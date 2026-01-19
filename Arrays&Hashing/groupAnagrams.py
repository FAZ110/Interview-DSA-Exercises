'''
Given an array of strings strs, group all anagrams 
together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same 
characters as another string, but the order of the characters can be different.
'''

# EXAMPLES

# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


# Input: strs = ["x"]
# Output: [["x"]]


# Input: strs = [""]
# Output: [[""]]


def groupAnagrams(strs):

    dic = {}

    for word in strs:

        letters = [0 for _ in range(26)]    # We will count every letter in word and then this array will be the key in the dictionary

        for letter in word:
            letters[ord(letter)-97] += 1    # letters in ASCII
        key = tuple(letters)

        if not key in dic:
            dic[key] = []
        dic[key].append(word)
    
    return list(dic.values())   # originally dictionary has key, value pairs we want list of values


            

