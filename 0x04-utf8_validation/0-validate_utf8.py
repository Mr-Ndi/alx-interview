#!/usr/bin/python3
''' UTF-8 Validation
'''
from typing import List


def validUTF8(data: List[int]) -> bool:
    ''' determines if a given data set
        represents a valid UTF-8 encoding
    '''
    if not isinstance(data, list) or\
            not all([isinstance(num, int) for num in data]):
        return False
    binary_list = [format(decimal_number % 256, '08b')
                   for decimal_number in data]
    i = 0
    while i < len(binary_list):
        byt = binary_list[i]
        if byt.startswith('0'):
            i = i + 1
        elif byt.startswith('110'):
            if len(binary_list) < i + 2:
                return False
            if not binary_list[i + 1].startswith('10'):
                return False
            i = i + 2
        elif byt.startswith('1110'):
            if len(binary_list) < i + 3:
                return False
            for j in range(i + 1, i + 3):
                if not binary_list[j].startswith('10'):
                    return False
            i = i + 3
        elif byt.startswith('11110'):
            if len(binary_list) < i + 4:
                return False
            for j in range(i + 1, i + 4):
                if not binary_list[j].startswith('10'):
                    return False
            i = i + 4
        else:
            return False
    return True
