#!/usr/bin/env python
# encoding: utf-8

##############################################
# use pin 11, not GPIO11, pin 11 egal GPIO17
#############################################
import RPi.GPIO as GPIO
import time
import sys

arg_len = len(sys.argv)
led_on = False

pin = 11;
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

for arg in sys.argv:
  print(arg)
  if arg == 'on':
    led_option = True
    break;
  else:
    led_option = False

if led_option == True:
  print("now led on")
  GPIO.output(pin, GPIO.HIGH)
else:
  print("now led off")
  GPIO.output(pin, GPIO.LOW)

#while True:
#  GPIO.output(pin, GPIO.LOW)
#  time.sleep(1)
#  GPIO.output(pin, GPIO.HIGH)
#  time.sleep(1)
#  count+=1
#  print("count")
#  print(count)
#  print("  ")
