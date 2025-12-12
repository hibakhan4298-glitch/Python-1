'''
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.

==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.

'''

# Ask user to enter an amount in one currency

exchange_rate = 0.92
usd_amount = float(input("Enter amount in USD: "))

# Convert the amount to another currency

eur_amount = usd_amount * exchange_rate

# Display the converted amount

print(f"{usd_amount} USD is equal to {eur_amount:.2f} EUR.")