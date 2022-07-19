def nearestValidPoint(self, x: int, y: int, points: list) -> int:
    """
    A point is valid if it shares the same x-coord or the same y-coord as your location (x, y)
    
    Return the index of the valid point with the smallest Manhattan distance from your current location. 
    
    If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

    The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
    """
    smallest_dist = float('inf')
    counter = -1
    index = -1
    
    for coord in points:
        counter += 1
        if coord[0] == x or coord[1] == y:
            cur_dist = abs(x - coord[0]) + abs(y - coord[1])
            if cur_dist < smallest_dist:
                smallest_dist = cur_dist
                index = counter

    return index
    
