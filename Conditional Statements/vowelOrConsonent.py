character = input("Enter a Character: ").lower()

if len(character) !=1 or not character.isalpha():
    print("Please enter valid single character !")
elif character in "aeiou":
    print(f"{character.upper()} is a Vowel")
else:
    print(f"{character.upper()} is a Consonent")


