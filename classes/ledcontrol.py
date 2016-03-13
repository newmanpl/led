class LedControl:
  def __init__(self):
    self.m_state = False
    self.m_led = -1

  def setState(self, on): # on: true/false
    self.m_state = on
  def getState(self):
    return self.m_state
  def getLed(self):
    return self.m_led
  def setLed(self, ledNr): # all: 0
    self.m_led = ledNr

