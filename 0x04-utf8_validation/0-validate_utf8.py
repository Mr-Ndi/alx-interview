#!/usr/bin/env python3

"""
    In this module there will be:
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need
    to handle the 8 least significant bits of each integer
"""


def validUTF8(data):

    """
        In this function we will:
            - Determine the number of bytes in the current UTF-8 character.
                - 1-byte character
                - 2-byte character
                - 3-byte character
                - 4-byte character
                else we will return Invalid leading byte
            - Check if there are enough bytes left for the character
            - Validate continuation bytes
            - Move to the next character
            - Continuation bytes must start with '10'
            - Return true for All characters are valid
    """
    length = len(data)
    i = 0

    while i < length:
        if data[i] & 0x80 == 0:
            bytes_to_process = 1
        elif data[i] & 0xE0 == 0xC0:
            bytes_to_process = 2
        elif data[i] & 0xF0 == 0xE0:
            bytes_to_process = 3
        elif data[i] & 0xF8 == 0xF0:
            bytes_to_process = 4
        else:
            return False
        if i + bytes_to_process > length:
            return False
        for j in range(1, bytes_to_process):
            if data[i + j] & 0xC0 != 0x80:
                return False
        i += bytes_to_process

    return True
