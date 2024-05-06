#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Function Description:
    - This function calculates the factorial
    of a non-negative integer using recursion.
    - Factorial of a non-negative integer
    'n' is the product of all positive integers less than or equal to 'n'.

    Parameters:
    - n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    - int: The factorial of the input integer.

    Raises:
    - ValueError: If the input integer is negative.
    """

    # Base case: If n is 0, return 1
    if n == 0:
        return 1
    else:
        # Recursive case: Return n multiplied by factorial of (n-1)
        return n * factorial(n-1)

# Accept the integer from command-line argument and calculate its factorial
f = factorial(int(sys.argv[1]))


# Print the calculated factorial
print(f)
