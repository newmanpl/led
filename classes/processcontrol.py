
class ProcessControl:
  def __init__(self):
    pass
  def writePidToFile(self, filename, pid):
    print("writePidToFile enter")
    target = open(filename , 'a')
    target.truncate()
    target.write(str(pid))
    target.close()

  def readPidFromFile(self, filename):
    try:
      with open(filename, 'r') as f:
        running_proc = f.readline().rstrip()
        return running_proc
    except IOError:
      print "[warning] first time the proc file is not existing"
      return 0

