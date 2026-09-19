# LEVEL 1: BASIC PATTERNS

print("1. Row-Number Triangle:")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

print()


print("2. Counting Triangle (Floyd's Triangle):")
n = 4
count = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(count, end=" ")
        count = count + 1
    print()

print()


print("3. Hollow Square Box:")
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Print star if on the top, bottom, left, or right border
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("")


# LEVEL 2: INTERMEDIATE PATTERNS

print("4. Diamond Pattern:")
n = 5

# Upper half of the diamond (including middle)
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
    # Print stars
    for k in range(1, (2 * i)):
        print("*", end="")
    print()

# Lower half of the diamond
for i in range(n - 1, 0, -1):
    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
    # Print stars
    for k in range(1, (2 * i)):
        print("*", end="")
    print()

print("")


print("5. Alphabet Right-Angled Triangle:")
n = 5
for i in range(1, n + 1):
    for j in range(0, i):
        # 65 is the starting number for uppercase 'A' in computer memory (ASCII)
        print(chr(65 + j), end=" ")
    print()

print("")


print("6. Hollow Pyramid:")
n = 5
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
        
    # Print stars and inner spaces
    for k in range(1, (2 * i)):
        # Star if first position, last position, or the very bottom row
        if k == 1 or k == (2 * i - 1) or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("")


# LEVEL 3: ADVANCED PATTERNS

print("7. Palindromic Number Pyramid:")
n = 5
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
        
    # Print increasing numbers for the left half
    for j in range(1, i + 1):
        print(j, end="")
        
    # Print decreasing numbers for the right half
    for j in range(i - 1, 0, -1):
        print(j, end="")
        
    print()

print("")


print("8. Butterfly Pattern:")
n = 4

# Upper half
for i in range(1, n + 1):
    # Left stars
    for j in range(1, i + 1):
        print("*", end="")
    # Middle spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    # Right stars
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Lower half
for i in range(n, 0, -1):
    # Left stars
    for j in range(1, i + 1):
        print("*", end="")
    # Middle spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    # Right stars
    for j in range(1, i + 1):
        print("*", end="")
    print()

print("")


print("9. Pascal's Triangle:")
n = 5
for i in range(0, n):
    # Print leading spaces for alignment
    for j in range(0, n - i - 1):
        print(" ", end="")
        
    val = 1
    for j in range(0, i + 1):
        print(val, end=" ")
        # Basic math logic to calculate the next number in the row
        val = val * (i - j) // (j + 1)
    print()