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
'''
method="notify_led_state"
proc=subprocess.Popen(['sudo php -f /var/www/phptest/php_server.php '+method],shell=True,stdout=subprocess.PIPE);
print("after popen");
response=proc.stdout.read();
print("after read");
print("response %s", response);
'''

setting = GPIOSetting()
setting.setMode(GPIO.BOARD)
setting.setWarnings(False)

Led1 = Led(16)
Led2 = Led(18)
Led3 = Led(40)

ledCtrl = LedControl()

for arg in sys.argv:
  if arg == 'looping':
    ledCtrl.setLed(0) #looping
  if arg == '1':
    ledCtrl.setLed(1)
  if arg == '2':
    ledCtrl.setLed(2)
  if arg == '3':
    ledCtrl.setLed(3)

  if arg == 'on':
    ledCtrl.setState(True)
  else:
    ledCtrl.setState(False)

file_location = '/var/www/phptest/proc'

procCtrl = ProcessControl()

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
  else:
    print("@@@ light 1 off")
    Led1.changeState(GPIO.LOW)

if ledCtrl.getLed() == 2:
  if ledCtrl.getState() == True:
    print("@@@ light 2\n")
    Led2.changeState(GPIO.HIGH)
  else:
    Led2.changeState(GPIO.LOW)

if ledCtrl.getLed() == 3:
  if ledCtrl.getState() == True:
    print("@@@ light 3\n")
    Led3.changeState(GPIO.HIGH)
  else:
    Led3.changeState(GPIO.LOW)

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
