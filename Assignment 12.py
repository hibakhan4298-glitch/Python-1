'''
Description: Develop a program that prompts the user to enter the
number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.

'''

# Ask the user for the number of rows

rows = int(input("Enter the number of rows: "))

# Display the right triangle

for i in range(1, rows + 1):
    print("*" * i)