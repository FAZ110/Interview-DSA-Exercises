'''
Given a binary string s without leading zeros, return 
true if s contains at most one contiguous segment 
of ones. Otherwise, return false.
'''

# EXAMPLES

# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.


# Input: s = "110"
# Output: true


def checkOnesSegment(s):

    flag = False
    for num in s:
        if num == '0':
            flag = True
        elif num == '1' and flag:
            return False
    
    return True
        

s = "1001"   
print(checkOnesSegment(s))