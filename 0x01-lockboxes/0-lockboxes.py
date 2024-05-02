#!/usr/bin/python3
'''LockBoxes Challenge'''


from collections import deque


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list where each inner list represents
                               the keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    # Number of boxes
    n = len(boxes)

    # Initialize a list to keep track of visited boxes
    visited = [False] * n
    visited[0] = True

    # Initialize a queue with the index of the first box (box 0)
    queue = deque([0])

    # Perform BFS traversal
    while queue:
        current_box = queue.popleft()
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # Check if the key opens a valid box and
            # that box has not been visited yet
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited
    return all(visited)
