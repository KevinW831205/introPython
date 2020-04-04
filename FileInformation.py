import os
import datetime

print(os.path.getsize("text.txt"))

timestamp = os.path.getmtime("text.txt");
print(timestamp)
datetimeTimeStamp =  datetime.datetime.fromtimestamp(timestamp)
print(datetimeTimeStamp)

absPath = os.path.abspath("text.txt")
print(absPath)