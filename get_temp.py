#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
from classes.gpiosetting import GPIOSetting
import time
import sys,os

setting = GPIOSetting()
setting.setMode(GPIO.BOARD)
setting.setWarnings(False)

GPIO.setup(16, GPIO.OUT)

maxheight = 50
minheight = 47

def rotate(start):
  if start == True:
     print("rotate true")
     GPIO.output(16, GPIO.HIGH)
  else: 
     GPIO.output(16, GPIO.LOW)

def get_cpu_temp():
  with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
    ret = float(f.read()) / 1000
  return ret

def autorun(t):
  try:
    if t > maxheight:
#      print("now start fan")
      rotate(True)
    else:
      if t < minheight:
#        print("now stop fan")
        rotate(False)

  except Exception, e:
    print("exception occurs==> %s", e)
    GPIO.cleanup()

for arg in sys.argv:
  if arg == 'cpu_temp':
    cpu_t = get_cpu_temp()
    print "temp : %.1f" %cpu_t
  if arg == 'autorun':
    cpu_t = get_cpu_temp()
    print "temp : %.1f" %cpu_t
    autorun(cpu_t)
