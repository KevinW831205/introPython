import re
import operator


class ErrorParser:
  errDict = {}
  def parseLine(self, line):
      result = re.search(r"ERROR (.*) \(",line)
      if not result is None:
        self.errDict[result.group(1)] = self.errDict.get(result.group(1),0) +1
  def sortedDict(self):
      return sorted(self.errDict.items(),key=operator.itemgetter(1),reverse=True)

class StatParser:
  infoDict = {}
  errDict = {}
  usernames = set()
  def parseLine(self,line):
      result = re.search(r"ERROR .* \(([\w]*)\)",line)
      if not result is None:
          self.errDict[result.group(1)] = self.errDict.get(result.group(1),0) +1
          self.usernames.add(result.group(1))

      result = re.search(r"INFO .* \(([\w]*)\)",line)
      if not result is None:
          self.infoDict[result.group(1)] = self.infoDict.get(result.group(1),0) +1
          self.usernames.add(result.group(1))


  def sortedDictionaries(self):
    userListSorted = sorted(self.usernames)
    result = []
    for user in userListSorted:
      result.append((user,self.infoDict.get(user,0),self.errDict.get(user,0)))
    return result