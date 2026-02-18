'''
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same 
length, return any one of them.
'''

# EXAMPLES

# Input: s = "ababd"
# Output: "bab"

# Input: s = "abbc"
# Output: "bb"





def longestPalindrome(s):
    n = len(s)

    resIdx = 0
    resLen = 0

    for i in range(n):
        # odd length
        l, r = i, i

        while l >= 0 and  r < n and s[l] == s[r]:
            if (r-l+1) > resLen:

                resIdx = l
                resLen = r-l+1
            l -= 1
            r += 1
        
        # even length
        l, r = i, i + 1

        while l >= 0 and  r < n and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resIdx = l
                resLen = r - l + 1
            l -= 1
            r += 1

    return s[resIdx: resIdx+resLen]
