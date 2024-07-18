def check_vowel_or_consonant(char):
    # Convert character to lowercase
    char = char.lower()
    
    # Check if the character is a vowel
    if char in 'aeiou':
        return f'{char} is a vowel.'
    else:
        return f'{char} is a consonant.'

# Take user input
character = input("Enter a character: ")

# Check if the input is a single character and alphabetic
if len(character) == 1 and character.isalpha():
    result = check_vowel_or_consonant(character)
    print(result)
else:
    print("Please enter a single alphabetical character.")
