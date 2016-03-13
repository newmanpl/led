import RPi.GPIO as GPIO

class Led:
  def __init__(self, pinNr):
    self.m_pin = pinNr
    GPIO.setup(pinNr, GPIO.OUT)

  def setPinNr(self, pinNr):
    self.m_pin = pinNr

  def getPinNr(self):
    return self.m_pin

  def resetPinPegel(self):
    GPIO.output(self.m_pin, GPIO.LOW)

  def changeState(self, newstate):
    GPIO.output(self.m_pin, newstate)

  def getState(self):
    return GPIO.input(self.m_pin)

