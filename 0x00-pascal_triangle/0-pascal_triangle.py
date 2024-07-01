#!/usr/bin/python3

"""
A function to make up apascal triangle.
# """


def pascal_triangle(n):
    """
    Description:
    n: this is the number of row that make up our triangle.
    in case n is less then 0 empty [triangle] list is returned.
    otherwise pascal_triangle.

    """
    if n <= 0:
        return []

    result = [[1]]
    for elem in range(1, n):
        row_list = [1]
        for ele in range(1, elem):
            row_list.append(result[elem-1][ele-1] + result[elem-1][ele])
        row_list.append(1)
        result.append(row_list)
    return result
