import os
print(os.getcwd())
if not os.path.isdir("newDir"):
    os.mkdir("newDir")


os.chdir("newDir")
print(os.getcwd())

if not os.path.isdir("dirception"):
    os.mkdir("dirception")

if not os.path.isdir("torm"):
    os.mkdir("torm")

if os.path.isdir("torm"):
    os.rmdir("torm")
os.chdir('../')
print(os.getcwd())


dir = "newDir"
dirList = os.listdir(dir)
print(dirList)

for name in dirList:
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))