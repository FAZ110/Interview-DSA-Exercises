'''
You are given a string digits made up of digits from 2 through 9 inclusive.
Each digit (not including 1) is mapped to a set of characters as shown below:
A digit could represent any one of the characters it maps to.
Return all possible letter combinations that digits could represent. You may return the answer in any order.
'''

# EXAMPLES

# Input: digits = "34"

# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

# Input: digits = ""

# Output: []


def letterCombinations(digits):
    n = len(digits)

    if n == 0:
        return []
    
    phone = {   # We create a map for digits and letters
            "0": ["+"],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
    
    res = []
    def rek(formed, index):
        if index == n:
            res.append(formed)
            return
        
        for letter in phone[digits[index]]: # use the map to form every possible word

            rek(formed+letter, index+1)
    
    rek('', 0)
    return res


digits = ""
print(letterCombinations(digits))
