file = open("text.txt")

print(file.readline())
file.close()

file = open("text.txt")
print(file.read());

file.close()

with open("text.txt") as file:
    print(file.read())

print("\n============")
with open("text.txt") as file:
    for line in file:
        print(line.strip().upper())

print("\n============")
file = open("text.txt")
lines = file.readlines()
file.close()

for line in lines:
    line.capitalize()
print(lines)

