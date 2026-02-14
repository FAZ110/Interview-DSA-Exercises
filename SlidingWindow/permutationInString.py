'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, 
then return true.

Both strings only contain lowercase letters.
'''

# EXAMPLES

# Input: s1 = "abc", s2 = "lecabee"
# Output: true

# Input: s1 = "abc", s2 = "lecaabee"
# Output: false



def checkInclusion(s1, s2):
    def check0(A):          # helper function to check if current array letters includes only 0's, then we have a permutation and return True
        for elem in A:
            if elem != 0:
                return False
        return True

    n = len(s2)
    m = len(s1)

    if m > n:   # If s1 is longer than s2 then we can't have a permutation 
        return False
    
    letters = [0 for _ in range(26)]    # to count letters

    for i in range(m):
        letters[ord(s1[i])-97] += 1     # count for letters in the s1
    

    for i in range(m):
        letters[ord(s2[i])-97] -= 1     # compute the first range in s2 from (0,m), the permutation has to have length of s1

    if check0(letters):     # check if the first letters are the permutation
        return True
    
    l = 0
    
    for r in range(m, n):   # we move the window one by one to the right, the length of the window never changes
        
        letters[ord(s2[r])-97] -= 1
        letters[ord(s2[l])-97] += 1
        l += 1

        if check0(letters): # if we found the permutation when return True
            return True

    return False


    
s1 = "abc"
s2 = "lecabee"

print(checkInclusion(s1, s2))