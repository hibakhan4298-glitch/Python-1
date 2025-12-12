'''
Description: Develop a function called is_prime that takes a positive integer as input and
returns True if it is a prime number, and False otherwise.

'''

# Check is the number is prime or not

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

# Enter a number to check if it is prime or not

num = int(input("Enter a number: "))
print(is_prime(num))