'''
You are given a string s consisting of only uppercase english 
characters and an integer k. You can choose up to k characters 
of the string and replace them with any other uppercase English
character.

After performing at most k replacements, return the length of 
the longest substring which contains only one distinct character.
'''

# EXAMPLES

# Input: s = "XYYX", k = 2
# Output: 4

# Input: s = "AAABABB", k = 1
# Output: 5

# IDEA
'''
We keep track of the characters inside the window. Number of characters we need 
to replaced are calculated witch this equation window_len - most_frequent_character,
if the value of this is greater than k we shift the window to the right (! not while loop, only if),
else we expand the window to the right.

!! There will be some iterations that will have invalid substrings but it is okay,
we only care about the length
'''



def characterReplacement(s, k):
    n = len(s)
    letters = {}    # Keep track of letters inside the window

    max_len = 0
    l = 0

    for r in range(n):
        letters[s[r]] = letters.get(s[r], 0) + 1

        most_frequent = max(letters.values())
        window_len = r-l+1
        
        if window_len-most_frequent > k:    # !!! if works instead of while because ex. if we have max_len=4 we do not care about length 3 or 2, we only expand the window or it stays the same size, just shifts to the right
            letters[s[l]] -= 1
            l +=1
        
        max_len = max(max_len, r-l+1)
    
    return max_len

s = "XYYX"
k = 2

s = "AAABABB"
k = 1
print(characterReplacement(s, k))


