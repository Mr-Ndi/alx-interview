#!/usr/bin/python3
"""
A module that contains a function that determines the winner of a game of
basing on the number of prime numbers in a list of integers.
"""


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task

    """
    def is_prime(n):
        """Check if a number is prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_count(n):
        """Count the number of prime numbers"""
        count = 0
        for i in range(1, n + 1):
            if is_prime(i):
                count += 1
        return count

    if prime_count(max(nums)) * 2 > sum(nums):
        return "Maria"
    return "Ben"
