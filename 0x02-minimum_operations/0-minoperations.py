#!/usr/bin/python3
"""
This is the function that solves the Minimum Operations problem.
"""


def minOperations(n: int) -> int:
    """
    Finds the minimum number of operations (Copy All and Paste) required
    to obtain n characters in the text file.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations
            required, or 0 if it's impossible to achieve.
    """
    if n <= 1:
        return 0
    # Find the largest divisor of n that is less than n
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor + minOperations(n // divisor)
        divisor += 1
    return n
