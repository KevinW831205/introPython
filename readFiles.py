file = open("text.txt")

print(file.readline())
file.close()

file = open("text.txt")
print(file.read());

file.close()

with open("text.txt") as file:
    print(file.read())
