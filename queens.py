class Solution:
    DistinctCounter = 0
    
    def __init__(self, n):
        self.board = self.createEmpty(n)
        self.checkQueens(0,0,n)
        print(self.board)
        
    def createEmpty(self,n):
        return [[0 for i in range(n)] for j in range(n)]

    def isValid(self, r, c, n): #the way this is implemented, immediately fails it if there is 1 queen inside, regardless of position
        for i in range(n):
            if self.board[r][i] == 1:
                return False
        for j in range(n):
            if self.board[j][c] == 1:
                return False
        for i in range(-n,n):
            if 0 <= r+i and r+i < n and 0<=c+i and c+i<n:
                if self.board[r+i][c+i] == 1:
                    return False
            if 0 <= r+i and r+i < n and 0<=c-i and c-i<n:
                if self.board[r+i][c-i] == 1:
                    return False
        return True
    
    
    def checkQueens(self, placed, rMin, n):
        if placed == n:
            self.DistinctCounter += 1
            return True
        for r in range(rMin, n): #row value
            for c in range(n): #col value
                if self.isValid(r, c, n):
                    self.board[r][c] = 1
                    if self.checkQueens(placed + 1, r + 1, n):
                        return True
                    self.board[r][c] = 0
            return False

n = 5
x = Solution(n)
##print(x.board)

##board = x.createEmpty(n)
##board = [[0,0,0,0,0],
##         [0,0,0,0,0],
##         [0,0,0,0,0],
##         [0,0,0,0,0],
##         [0,0,0,0,0]]
##x.checkQueens(board, 0, 0, n)
##print(board)

    
