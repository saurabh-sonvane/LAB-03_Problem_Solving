string = input("Enter the string: ")
character = input("Enter the character you want to count in string: ")

count = 0

for i in string:
    if i == character:
        count += 1

print(count)