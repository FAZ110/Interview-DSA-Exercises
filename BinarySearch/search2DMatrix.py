'''
You are given an m x n 2-D integer array matrix and an integer target.

    -Each row in matrix is sorted in non-decreasing order.
    -The first integer of every row is greater than the last integer of 
    the previous row.

Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
'''

# EXAMPLES

# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# Output: true

# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
# Output: false


# IDEA
'''
We use binary search twice, firstly to find the correct row which is represented 
by boundary values (x, y), such as x < target < y, then on that row we use another
binary search to fing the target 
'''

def searchMatrix(matrix, target):
    

    l, r = 0, len(matrix)-1
    row = 0

    while l < r:

        mid = (l+r)//2

        if matrix[mid][0] == target or matrix[mid][-1] == target:
            return True
        elif matrix[mid][0] < target and matrix[mid][-1] > target:
            row = mid
            break
        elif matrix[mid][0] < target and matrix[mid][-1] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    l, r = 0, len(matrix[0])-1

    while l <= r:

        mid = (l+r)//2
        print(mid)

        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False


        
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 12

matrix = [[1]]
target = 1

print(searchMatrix(matrix, target))

