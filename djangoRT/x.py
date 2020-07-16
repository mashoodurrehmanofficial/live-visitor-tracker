import os

mem=str(os.popen('free -t -m').readlines())
#print results
print("CPU Usage = " + mem)