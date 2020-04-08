import csv
from logparser import ErrorParser, StatParser

ep = ErrorParser()
sp = StatParser()

with open("log.log",'r') as file:
  for line in file:
    ep.parseLine(line)
    sp.parseLine(line)

with open('error_message.csv', "w", newline='') as errorCSV:
  writer = csv.writer(errorCSV)
  writer.writerow(["Error","Count"])
  writer.writerows(ep.sortedDict())

with open('user_statistics.csv',"w", newline='') as statCSV:
  writer = csv.writer(statCSV)
  writer.writerow(["Username","INFO","ERROR"])
  writer.writerows(sp.sortedDictionaries())


