string = input("Enter a string: ")
vowel_count = 0
consonant_count = 0

for character in string:
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
        vowel_count += 1
    elif 'a' <= character <= 'z':
        consonant_count += 1

print(f'Total no. of vowels are {vowel_count}')
print(f'Total no. of consonants are {consonant_count}')
