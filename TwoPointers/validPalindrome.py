'''
Given a string s, return true if it is a palindrome, otherwise 
return false.

A palindrome is a string that reads the same forward and 
backward. It is also case-insensitive and ignores all 
non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) 
and numbers (0-9).
'''

# EXAMPLES

# Input: s = "Was it a car or a cat I saw?"

# Output: true


# Input: s = "tab a cat"

# Output: false



def isPalindrome(s):
    n = len(s)
    s = s.lower()
    l,r = 0,len(s)-1
    

    while l < r:

        while l < n-1 and (s[l] == ' ' or not s[l].isalnum()):
            l += 1
        while r > 0 and (s[r] == ' 'or not s[r].isalnum()):
            r -= 1

        if l >= r:
            return True
        
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1
    
    return True

s = "Was it a car or a cat I saw?"
# s = "tab a cat"
# s=".,"
print(isPalindrome(s))



# ALTERNATIVE
# Cleaner version without nested while loops

def isPalindrome(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
            
    return True

        

