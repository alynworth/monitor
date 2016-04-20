import time
import glob

def main():

  subprocess.call ("sudo", "modprobe", "w1-gpio")
  subprocess.call ("sudo", "modprobe", "w1-therm")
  subprocess.call ("sudo", "cd", "/sys/bus/w1/devices/")
  subprocess.call ("ls")

devicelist = glob.glob('/sys/bus/w1/devices/28*')
if devicelist=='':
  print "None"
else:
  # append /w1slave to the device file
  sensor=devicelist[0]
  w1devicefile = devicelist[0] + '/w1_slave'
  print sensor [20:]
  f = open (w1devicefile, 'r')
  print f.read()
  f.close()
  
  sensor=devicelist[1]
  w1devicefile = devicelist[1] + '/w1_slave'
  print sensor [20:]
  f = open (w1devicefile, 'r')
  print f.read()
  f.close()








