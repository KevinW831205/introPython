import os

with open("textToDelete.txt", "w") as file:
    file.write("new text file");

os.remove("textToDelete.txt")


# os.rename("text2.txt","text3.txt");

def renameText2and3():
    if os.path.exists("text2.txt"):
        os.rename("text2.txt", "text3.txt")
    elif os.path.exists("text3.txt"):
        os.rename("text3.txt", "text2.txt")


renameText2and3()
