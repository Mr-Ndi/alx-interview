#!/usr/bin/python3

"""
    A module for lockboxes algorithm
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of list of int): A list where each index represents a box and
    the list at each index contains the keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    opened_boxes = set([0])
    for box_index, keys in enumerate(boxes):
        if box_index not in opened_boxes:
            continue
        for key in keys:
            if 0 <= key < n:
                opened_boxes.add(key)
    return len(opened_boxes) == n
