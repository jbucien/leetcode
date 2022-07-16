def subtractProductAndSum(n: int) -> int:
    """
    Given an integer number n, return the difference between the product of its digits and the sum of() its digits.
    """
    n = str(n)
    sum = 0
    prod = 1
    for digit in n:
        sum+= int(digit)
        prod *= int(digit)
    return (prod - sum)