'''
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.

'''

# The input section is below

weight_input = input("Enter your weight in kilos: ")
height_input = input("Enter your height in meters: ")

# Conversion to float is calculated below

weight = float(weight_input)
height = float(height_input)

# Calculate the BMI processing below

bmi = weight / (height ** 2)

# Ouput below

print("The BMI is: ", bmi)

