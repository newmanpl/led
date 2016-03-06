#!/usr/bin/env python
# encoding: utf-8

########################################################################
# use pin 11, not GPIO11, pin 11 egal to GPIO17, pin16 egual to GPIO 23
# use pin 18, equal to GPIO 24
#########################################################################
import RPi.GPIO as GPIO
import time
import sys,os
import thread
import psutil
import subprocess
from os import getpid

method="notify_led_state" 
proc=subprocess.Popen(['sudo php -f /var/www/phptest/php_server.php '+method],shell=True,stdout=subprocess.PIPE); 
print("after popen");
response=proc.stdout.read();
print("after read");
print("response %s", response);

arg_len = len(sys.argv)
led_on = False
led_looping = False
led_which = 1
pin1 = 16
pin2 = 18
pin3 = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
print "enter python \r",
for arg in sys.argv:
  if arg == 'looping':
    led_looping = True
  if arg == '1':
    led_which = 1
  if arg == '2':
    led_which = 2
  if arg == '3':
    led_which = 3

  print("which led %d\r", led_which),

  if arg == 'on':
    led_on = True
  else:
    led_on = False

file_location = '/var/www/phptest/proc'
file_existing = False
try:
  with open(file_location, 'r') as f:
    running_proc = f.readline().rstrip()
    file_existing = True
    if led_looping and led_on and file_existing :
      exit()
except IOError:
  print "[warning] first time the proc file is not existing"

try:
  if file_existing:
    cmd = "sudo kill " + running_proc
    print("cmd %s\n",cmd)
    os.system(cmd)
except:
  print("[warning] proc is not existing")

mypid = getpid()
print("current pid %d\n",mypid)
target = open("/var/www/phptest/proc", 'a')
target.truncate()
target.write(str(mypid))
target.close()


def wait_for_input(stop):
    print("enter wait_for_input\n")
    if led_on == False:
      print("now callback stop looping\n")
      stop.append(True)
      led_reset()
      GPIO.cleanup()

def led_reset():
#    print("@@@ enter reset led\n")
    led_looping = False
    led_on = False
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.LOW)

def blink():
    stop = []
    print("call blink \r"),
    while led_looping == True and led_on == True:
      print("enter while led_looping %d led_on %d \r", led_looping, led_on),
      led_reset()
      GPIO.output(pin1, GPIO.HIGH)
      time.sleep(1)
      led_reset()
      GPIO.output(pin2, GPIO.HIGH)
      time.sleep(1)
      led_reset()
      GPIO.output(pin3, GPIO.HIGH)
      time.sleep(1)
print("led_looping %d led on %d\n", led_looping, led_on),

###################################################
# handle single light
####################################################
#led_reset()
if led_which == 1:
  if led_on == True:
    print("@@@ light 1\n")
    GPIO.output(pin1, GPIO.HIGH)
  else:
    print("@@@ light 1 off")
    GPIO.output(pin1, GPIO.LOW)
if led_which == 2:
  if led_on == True:
    print("@@@ light 2\n")
    GPIO.output(pin2, GPIO.HIGH)
  else:
    GPIO.output(pin2, GPIO.LOW)

if led_which == 3:
  if led_on == True:
    print("@@@ light 3\n")
    GPIO.output(pin3, GPIO.HIGH)
  else:
    GPIO.output(pin3, GPIO.LOW)

if led_looping == True and led_on == True:
  print("start looping\r"),
#  thread.start_new_thread(blink, ())
#  time.sleep(2)
  blink()

if led_looping == True and led_on == False:
  print("@@ stop looping\r"),
  led_reset()
  GPIO.cleanup()
cmd = 'sudo rm ' + file_location
os.system(cmd)
#call php back
#thread.join()
print("3 reach end of py endline led_looping %d\r", led_looping)
