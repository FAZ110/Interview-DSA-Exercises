'''
Given a 2-D grid of characters board and a string word, return true if 
the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path 
in the board with horizontally or vertically neighboring cells. 
The same cell may not be used more than once in a word.
'''

# EXAMPLE

# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"

# Output: true


# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"

# Output: false

# IDEA
'''
We start searching from the cell that has letter word[0], after that we 
are recursively checking each neighbouring cell marking visited ones
as '#' to not visit it again, If r or c are out of boundaries we return False
for that part of a recursion tree
'''

def exist(board, word):
    n = len(board)
    m = len(board[0])


    def rek(r, c, index):
        if index == len(word):
            return True
        
        if (r < 0 or r >= n or c < 0 or c >= m or board[r][c] != word[index]):
            return False
        
        temp = board[r][c]
        board[r][c] = '#'

        found = (rek(r + 1, c, index + 1) or
                 rek(r - 1, c, index + 1) or 
                 rek(r, c + 1, index + 1) or
                 rek(r, c - 1, index + 1))

        board[r][c] = temp
        return found
        
    

    for i in range(n):
        for j in range(m):
            print(i,j)
            if board[i][j] == word[0]:
                if rek(i, j, 0):
                    return True
    return False


board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"

print(exist(board, word))