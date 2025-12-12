'''
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.

'''

# Enter a time duration in hours

seconds = int(input("Enter the time in seconds: "))

hours = seconds // 3600

# Convert the time duration to minutes and seconds

minutes = seconds % 3600 // 60
new_seconds = seconds % 60

# Display the converted time duration in minutes and seconds

print(f"The converted time is {hours}:hours, {minutes}:minutes and {new_seconds}:seconds.")