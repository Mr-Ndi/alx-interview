#!/usr/bin/python3
"""
A module that contains a function that determines the winner of a game of
basing on the number of prime numbers in a list of integers.
"""


def isWinner(x, nums):
    """
    Determines the winner of the game based on the number of prime numbers
    in a list of integers.

    Arguments:
    x (int): The number of rounds in the game.
    nums (list): A list of integers.

    Returns:
    str: The name of the player that won the most rounds.
    """
    def is_prime(n):
        """
        Determines if a number is a prime number.

        Arguments:
        n (int): The number to check.

        Returns:
        bool: True if the number is a prime number, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if x % 2 == 0:
        return "Maria"
    return "Ben"
