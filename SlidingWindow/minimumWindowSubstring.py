'''
Given two strings s and t, return the shortest substring of s such that 
every character in t, including duplicates, is present in the substring. 
If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
'''

# EXAMPLES

# Input: s = "OUZODYXAZV", t = "XYZ"
# Output: "YXAZ"

# Input: s = "xyz", t = "xyz"
# Output: "xyz"

# Input: s = "x", t = "xy"
# Output: ""


def minWindow(s, t):

    if t == "": return ""

    countT, window = {}, {} # countT is the goal map, window is the map of current window letters

    for c in t:
        countT[c] = countT.get(c, 0) + 1
    
    have, need = 0, len(countT) # have is a counter of how many unique characters in our window have met or exceeded the required count in t
                                # need is a total number of unique characters in t
    res, resLen = [-1,-1], float('inf')

    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        # If this char matches expectation in countT, we "satisfied" one requirement
        if c in countT and window[c] == countT[c]:
            have += 1
        
        # 3. While Valid: Shrink from Left
        while have == need:
            
            # Update result if this window is smaller
            if (r-l+1) < resLen:
                res = [l, r]
                resLen = r-l+1
            # Pop from the left to shrink
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    
    l,r = res

    return s[l:r+1] if resLen != float('inf') else ""


s = "OUZODYXAZV"
t = "XYZ"
print(minWindow(s, t))


