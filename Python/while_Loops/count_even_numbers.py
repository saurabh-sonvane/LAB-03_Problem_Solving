n = int(input("Enter n: "))
even_count = 0
number = 1
while number <= n:
    if number % 2 == 0:
        even_count += 1
    number += 1
print("Number of even numbers:", even_count)
