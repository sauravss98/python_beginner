import time
ct=time.localtime(time.time())
gmt=time.gmtime(time.time())
print("GMT time: ",gmt.tm_hour,":",gmt.tm_min,":",gmt.tm_sec)

print("Current time",ct.tm_hour,":",ct.tm_min,":",ct.tm_sec)
