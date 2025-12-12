'''
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.

'''

# Enter a year

year = int(input("Enter a year: "))

# Is the year a leap year or not

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "Is a leap year."
else:
    result = "Is not a leap year."

# Display wheather the entered year is a leap year or not

print(f"{year} {result}")