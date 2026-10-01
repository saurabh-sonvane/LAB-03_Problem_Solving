n = int(input("Enter n: "))
if n > 0:
    row = 1
    while row <= n:
        number = 1
        while number <= row:
            print(number, end=" ")
            number += 1
        print()
        row += 1
else:
    print("Enter a positive integer.")
