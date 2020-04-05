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