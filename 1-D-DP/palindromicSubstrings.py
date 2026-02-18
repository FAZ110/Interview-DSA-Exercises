'''
Given a string s, return the number of substrings within s that are 
palindromes.

A palindrome is a string that reads the same forward and backward.
'''

# EXAMPLES

# Input: s = "abc"
# Output: 3

# Input: s = "aaa"
# Output: 6

# IDEA

'''
Logic is pretty much the same as is longestPalindromicSubstring
'''

def countSubstrings(s):
    n = len(s)

    res = 0

    for i in range(n):
        # odd length
        l, r = i, i

        while l >= 0 and r < n and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        # even length
        l,r = i, i+1

        while l >= 0 and r < n and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
    
    return res




s = "abc"
print(countSubstrings(s))