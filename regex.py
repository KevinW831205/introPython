import re
result = re.search(r"aza","plaza")
print(result)
result = re.search(r"aza","bazaar")
print(result)
result = re.search(r"aza","maze")
print(result)

print(re.search(r"^x","xav"))
print(result)

print(re.search(r"p.ng","penguin"))
print(re.search(r"p.ng","ping"))
print(re.search(r"p.ng","pinng"))


print(re.search("[a-z]way","away the highway"))
print(re.search("cloud[a-zA-Z0-9]","cloudy"))
print(re.search("cloud[a-zA-Z0-9]","cloud9"))
print(re.search("cloud[a-zA-Z0-9]","cloud!"))
print(re.search(r"[^a-zA-Z! ]","asd g"))
print(re.search(r"cat|dog","somecat"))
print(re.search(r"cat|dog","somedog"))
print(re.findall(r"cat|dog","somedog somecat somdog"))
print(re.search(r"ab.*n","abn"))
print(re.search(r"ab.*n","abogn"))
print(re.search(r"ab.*n","abognin"))
print(re.search(r"o+l+","goldfish"));
print(re.search(r"o+l+","gooooldfish"));
print(re.search(r"o+l+","goooodlfish"));
print(re.search(r"ab?a","aaa"))
print(re.search(r"ab?a","abaa"))