'''
Given a string s, split s into substrings where every substring is 
a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.
'''

# EXAMPLES

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Input: s = "a"
# Output: [["a"]]

# IDEA
'''
in rek we make a decision for every valid cut to add it to palindromes
'''

def partition(s):
    def isPalindrome(word):
        return word == word[::-1]
    
    n = len(s)

    res = []

    def rek(index, palindromes):
        if index == n:
            res.append(palindromes[::])
            return
        
        for end in range(index+1, n+1): # from index to end we search for valid palindromes. If s[index:end] is a palindrome we add it to our list and move on with recursion
            substring = s[index:end]

            if isPalindrome(substring):
                palindromes.append(substring)

                rek(end, palindromes)

                palindromes.pop()
    
    rek(0, [])
    return res
        
s = "aab"
print(partition(s))

        
