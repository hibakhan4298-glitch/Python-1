'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.

=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.

'''
# Ask the user to enter the length and width of a rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle

area = length * width

# Display the calculated area of the rectangle

print(f"The area of the rectangle is: {area}")
