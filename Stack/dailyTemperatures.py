'''
You are given an array of integers temperatures where 
temperatures[i] represents the daily temperatures on 
the ith day.

Return an array result where result[i] is the number of 
days after the ith day before a warmer temperature appears 
on a future day. If there is no day in the future where a 
warmer temperature will appear for the ith day, set result[i] 
to 0 instead.
'''


# EXAMPLES

# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

# Input: temperatures = [22,21,20]
# Output: [0,0,0]


def dailyTemperatures(temperatures):
    n = len(temperatures)

    stack = []      # We use a stack
    res = [0 for _ in range(n)]

    for i in range(n):
        
        while len(stack) > 0 and temperatures[i] > stack[-1][0]:    # Everytime when stack is not empty and we have bigger temperature than the one on the top of the stack, we found the day we were looking for. We use while loop to catch every possible day that is on the stack wicth smaller temperature.

            _, index = stack.pop()
            res[index] = i - index
        
        stack.append((temperatures[i], i))  # After while loop we have to add current value on the stack
    
    return res


temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))

