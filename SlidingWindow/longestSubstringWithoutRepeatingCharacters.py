'''
Given a string s, find the length of the longest substring 
without duplicate characters.

A substring is a contiguous sequence of characters within a 
string.
'''

# EXAMPLES

# Input: s = "zxyzxyz"
# Output: 3

# Input: s = "xxxx"
# Output: 1


def lengthOfLongestSubstring(s):
    n = len(s)

    letters = {}    # We will keep track of characters in the substring in the dictionary
    max_len = 0

    l = 0

    for r in range(n):
        letters[s[r]] = letters.get(s[r], 0) + 1 # Add current character

        while letters[s[r]] > 1:    # If the current character count is > 1 then we have to move l boundary to make a substring viable

            letters[s[l]] -= 1
            l += 1
        max_len = max(max_len, r-l+1) # When we have viable substring, we calculate the length
    
    return max_len

s = "zxyzxyz"
s = "xxxx"
print(lengthOfLongestSubstring(s))