'''
You are given a string s consisting of the 
following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
'''

# EXAMPLES

# Input: s = "[]"
# Output: true

# Input: s = "([{}])"
# Output: true

# Input: s = "[(])"
# Output: false


def isValid(s):
    brackets = {")":"(", "]":"[", "}":"{"}  # We define the bracket matches (closing bracket has to match the opening one)
    stack = []

    for char in s:

        if char in brackets:
            top_element = stack.pop() if stack else "#"

            if top_element != brackets[char]:   # if the type do not match then false
                return False
        else:
            stack.append(char)
    
    return not stack    # if at the end the stack is not empty we have brackets that are not closed/opened


s = "([{}])"
print(isValid(s))