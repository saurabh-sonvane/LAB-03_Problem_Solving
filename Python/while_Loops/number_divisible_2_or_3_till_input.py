n = int(input("Enter n: "))
number = 1
while number <= n:
    if number % 2 == 0 and number % 3 == 0:
        print(number)
    number += 1
