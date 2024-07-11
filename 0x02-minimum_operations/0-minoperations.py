#!/usr/bin/python3


def minOperations(n: int):
    if n <= 1:
        return 0
    # Find the largest divisor of n that is less than n
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor + minOperations(n // divisor)
        divisor += 1
    return n
