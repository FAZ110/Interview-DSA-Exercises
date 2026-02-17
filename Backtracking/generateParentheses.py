'''
You are given an integer n. Return all well-formed 
parentheses strings that you can generate with n pairs of parentheses.
'''

# EXAMPLES

# Input: n = 1
# Output: ["()"]

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# We can only add ')' if there are some unused '('. We can start from formed = '(' and build more from this template

def generateParenthesis(n):
    res = []


    def rek(formed, opened, total):
        if total == n and opened == 0:
            res.append(formed[::])
            return
        if opened > n or total > n:
            return
        
        if opened > 0:
            rek(formed+')', opened - 1, total + 1)
            rek(formed+'(', opened + 1, total)
        else:
            rek(formed+'(', opened + 1, total)
    
    rek('(', 1, 0)

    return res


n = 3
print(generateParenthesis(n))





# ALTERNATIVE

def generateParenthesis(n):
    res = []

    def rek(total, openp, paren):
        if total == n*2:
            res.append(paren)
            return
        
        
        if openp == n:
            rek(total+1, openp, paren+")")
        else:
            rek(total+1, openp+1, paren+"(")
            if total - openp < openp:
                rek(total+1, openp, paren+")")
        
    rek(1, 1, "(")
    return res