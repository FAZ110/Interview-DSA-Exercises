'''
Given two strings text1 and text2, return the length of the longest 
common subsequence between the two strings if one exists, otherwise 
return 0.

A subsequence is a sequence that can be derived from the given 
sequence by deleting some or no elements without changing the 
relative order of the remaining characters.

    For example, "cat" is a subsequence of "crabt".

A common subsequence of two strings is a subsequence that exists in 
both strings.
'''

# EXAMPLES

# Input: text1 = "cat", text2 = "crabt" 
# Output: 3 

# Input: text1 = "abcd", text2 = "abcd"
# Output: 4

# Input: text1 = "abcd", text2 = "efgh"
# Output: 0

# IDEA
'''
To solve this efficiently, we build a 2D table where each cell represents a sub-calculation:
Matching Characters: If the characters at the current position match, we look at the diagonal value (the result without these two characters) and add 1.
Mismatched Characters: If they don't match, we take the maximum value from either the cell directly above or the cell to the left.
'''

def longestCommonSubsequence(text1, text2):

    m, n = len(text1), len(text2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


text1 = "cat"
text2 = "crabt"

print(longestCommonSubsequence(text1, text2))