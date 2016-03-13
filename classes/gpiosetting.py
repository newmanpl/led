#!/usr/bin/env python
# encoding: utf-8

########################################################################
# use pin 11, not GPIO11, pin 11 egal to GPIO17, g_pin16 egual to GPIO 23
# use pin 18, equal to GPIO 24
#########################################################################

import RPi.GPIO as GPIO

class GPIOSetting:
  def __init__(self):
    pass
  def setMode(self,mode):
    GPIO.setmode(mode)
  def setWarnings(self,warning):
    GPIO.setwarnings(warning)

  def setOutPin1(self, pin, mode):
    print("set pin1")
    self.pin1 = pin
    GPIO.setup(pin, mode)
  def setOutPin2(self, pin, mode):
    self.pin2 = pin
    GPIO.setup(pin, mode)
  def setOutPin3(self, pin, mode):
    self.pin3 = pin
    GPIO.setup(pin, mode)

  def getOutPin1(self):
    return self.pin1
  def getOutPin2(self):
    return self.pin2
  def getOutPin3(self):
    return self.pin3

