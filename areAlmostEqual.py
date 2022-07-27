def areAlmostEqual(s1: str, s2: str) -> bool:
    """
    You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
    
    Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
    """
    # Scenario 1 -- all character are the same 
    # Scenario 2 -- all characters except 2 are the same 
    # All other scenarios FALSE

    diff = 0
    index1 = 0
    index2 = 0
    for index, letter in enumerate(s1):
        if letter != s2[index]:
            diff += 1
            if diff == 1:
                index1 = index
            elif diff == 2:
                index2 = index
            else:
                return False
    if s1[index1] == s2[index2] and s1[index2] == s2[index1]:
            return True
    else:
        return False


print(areAlmostEqual("bank", "kanb"))
print(areAlmostEqual("kelb", "kelb"))
print(areAlmostEqual("quota", "atouq"))
print(areAlmostEqual("hphyrlaftwzdyscbrraxajeevycarzovuwxazqhrzjuxwqeoqwhwxgvxgfz", 
"hhzxqgvwqpxrwcwfjuaquvhzcogexayjzrebahfsxdwreytraxzvlrwoyaz")
)
print(areAlmostEqual("ab", "aa"))