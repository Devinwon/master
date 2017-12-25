import time
print("--start--")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
print("--5s after--")
time.sleep(5)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
print("--end--")
