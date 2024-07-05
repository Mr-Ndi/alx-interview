#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    opened_boxes = set([0])
    for box_index, keys in enumerate(boxes):
        if box_index not in opened_boxes:
            continue
        for key in keys:
            if 0 <= key < n:
                opened_boxes.add(key)
    return len(opened_boxes) == n
