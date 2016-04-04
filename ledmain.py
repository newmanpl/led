#!/usr/bin/env python
# encoding: utf-8

########################################################################
# use pin 11, not GPIO11, pin 11 egal to GPIO17, setting.getOutPin1()6 egual to GPIO 23
# use pin 18, equal to GPIO 24
#########################################################################

import RPi.GPIO as GPIO
from classes.gpiosetting import GPIOSetting
from classes.processcontrol import ProcessControl
from classes.ledcontrol import LedControl
from classes.Led import Led
import time
import sys,os
import thread
import psutil
import subprocess
from os import getpid
from subprocess import Popen,PIPE,STDOUT
import urllib
import MySQLdb
import datetime

class Database:

    host = 'localhost'
    user = 'root'
    password = 'pi'
    db = 'led'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()
        print self.connection
    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
def TimestampMillisec64():
      return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
def notify_server(db, id, newstate):
  cmd = "UPDATE tb_led SET state='%s'  WHERE id='%s'" % (newstate, id)
#  cmd = "update tb_led set state='off' where id='light2'"
  print cmd
  db.insert(cmd)
#  time_diff_file = '/var/www/phptest/timediff.txt'
#  procCtrl.writePidToFile(time_diff_file, TimestampMillisec64())
'''
  method="notify_led_state";
  cmd = 'php -f ./php_server.php' + ' ' +  method + ' ' + id + ' ' + state;
  proc=subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE);

  response=proc.stdout.read();

  print(response);
'''
procCtrl = ProcessControl()
time_diff_file = '/var/www/phptest/timediff.txt'
procCtrl.writePidToFile(time_diff_file, TimestampMillisec64())

setting = GPIOSetting()
setting.setMode(GPIO.BOARD)
setting.setWarnings(False)

Led1 = Led(16)
Led2 = Led(18)
Led3 = Led(40)

ledCtrl = LedControl()
db = Database()

for arg in sys.argv:
  if arg == 'looping':
    ledCtrl.setLed(0) #looping
  if arg == 'light1':
    ledCtrl.setLed(1)

  if arg == 'light2':
    ledCtrl.setLed(2)
  if arg == 'light3':
    ledCtrl.setLed(3)

  if arg == 'on':
    ledCtrl.setState(True)
  else:
    ledCtrl.setState(False)

file_location = '/var/www/phptest/proc'

#procCtrl = ProcessControl()

pid = procCtrl.readPidFromFile(file_location)
if pid != 0:
   cmd = "sudo kill " + pid
   print("cmd %s\n",cmd)
   os.system(cmd)

procCtrl.writePidToFile(file_location, getpid())

def led_reset():
#    print("@@@ enter reset led\n")
#    ledCtrl.setState(True)
#    ledCtrl.setLed(0)
    Led1.resetPinPegel()
    Led2.resetPinPegel()
    Led3.resetPinPegel()

def blink():
    while ledCtrl.getState() == True and ledCtrl.getLed() == 0:
      led_reset()
      Led1.changeState(GPIO.HIGH)
      time.sleep(0.5)
      led_reset()
      Led2.changeState(GPIO.HIGH)
      time.sleep(0.5)
      led_reset()
      Led3.changeState(GPIO.HIGH)
      time.sleep(0.5)
      print("######## blink: looping led %d state %d \n", ledCtrl.getLed(),ledCtrl.getState())

###################################################
# handle single light
####################################################
#led_reset()
print("######## led %d state %d \n", ledCtrl.getLed(),ledCtrl.getState())
if ledCtrl.getLed() == 1:
  if ledCtrl.getState() == True:
    print("@@@ light 1\n")
    Led1.changeState(GPIO.HIGH)
    notify_server(db, 'light1', 'on')
  else:
    print("@@@ light 1 off")
    Led1.changeState(GPIO.LOW)
    notify_server(db, 'light1', 'off')

if ledCtrl.getLed() == 2:
  if ledCtrl.getState() == True:
    print("@@@ light 2\n")
    Led2.changeState(GPIO.HIGH)
    notify_server(db, 'light2', 'on')
  else:
    Led2.changeState(GPIO.LOW)
    notify_server(db, 'light2', 'off')

if ledCtrl.getLed() == 3:
  if ledCtrl.getState() == True:
    print("@@@ light 3\n")
    Led3.changeState(GPIO.HIGH)
    notify_server(db, 'light3', 'on')
  else:
    Led3.changeState(GPIO.LOW)
    notify_server(db, 'light3', 'off')

if ledCtrl.getLed() == 0 and ledCtrl.getState() == True:
  blink()
else:
  print("### something is wrong ###\r\n")

if ledCtrl.getLed() == 0 and ledCtrl.getState() == False:
  print("@@ stop looping\r"),
  led_reset()
  GPIO.cleanup()
cmd = 'sudo rm ' + file_location
os.system(cmd)
#call php back
#thread.join()
#print("3 reach end of py endline g_led_looping %d\r", g_led_looping)
