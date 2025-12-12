'''
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.

=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.

'''
##############
# INPUT
#############

# Prompt the user to enter the principle amount

principle = float(input("enter the principle amount: "))

# Ask the user to enter the interest rate

rate = float(input("enter the interest rate (in percentage): "))

# Ask the user for the time period

time = float(input("enter the time period (in years): "))

#############
# PROCESSING
#############

# Calculate the simple interest

simple_interest = (principle * rate * time) / 100

##########
# OUTPUT
##########

print ("The calculated simple interest is:", simple_interest)




