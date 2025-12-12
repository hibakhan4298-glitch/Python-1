'''
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

'''

# Enter a string

text = input("Enter a string: ")

cleaned_text = text.replace(" ", "").lower()

# Check if it's a palindrome

if cleaned_text == cleaned_text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")

