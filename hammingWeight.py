def hammingWeight(n: int) -> int:
    """
    Takes an unsigned int and returns the number of '1' bits it has.
    """
    count = 0
    while n != 0:
        count += 1
        # Flips least sig bit to 0
        n &= (n-1)
    return count        