from functools import reduce 

# My initial solution (Brute Force)
def isHappy_brute(n:int) -> bool:
    """
    A happy number is a number defined by the following process:
        - Starting with any positive integer, replace the number by the sum of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    
    Return true if n is a happy number, and false if not.
    """
    results = []
    while True:
        get_digits = [int(num)**2 for num in str(n)]
        result = reduce(lambda a, b: a + b, get_digits)
        if result == 1:
            return True
        elif result in results:
            return False
        else:
            results.append(result)
            n = result


# Optimatization: Use Floyd's Cycle-Finding Algorithm
# O(logn) TC
# O(1) SC

def isHappy(n: int) -> bool:
  def get_next(number): # helper function that generates next number in linked list
    total_sum = 0
    while number > 0:
      number, digit = divmod(number, 10) # parses number into its digits
      total_sum += digit ** 2
    return total_sum
  
  turtle = n
  hare = get_next(n)
  while hare != 1 and turtle != hare:
    turtle = get_next(turtle)
    hare = get_next(get_next(hare))
  return hare == 1

print(isHappy(2))


