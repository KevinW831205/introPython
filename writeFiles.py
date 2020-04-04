with open("text2.txt", "w") as file:
    file.write("new text file")

with open("text2.txt", "w") as file:
    file.write("overwritting")

with open("text2.txt", "a") as file:
    file.write("\nappending")
