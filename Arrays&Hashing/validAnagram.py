'''
Given two strings s and t, return true if the two strings 
are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters 
as another string, but the order of the characters can be 
different.
'''

# EXAMPLES

# Input: s = "racecar", t = "carrace"
# Output: true

# Input: s = "jar", t = "jam"
# Output: false

def isAnagram(s, t):

    if len(s) != len(t):    # if lengths are different we can return False automatically
        return False

    letters = {}

    for letter in s:
        letters[letter] = letters.get(letter, 0) + 1

    for check in t:
        if check not in letters or letters[check] == 0:
            return False
        
        letters[check] -= 1
    
    return True


s = "racecar"
t = "carrace"

print(isAnagram(s, t))
