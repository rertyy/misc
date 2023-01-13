def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])

        #check last row for 0s
        if matrix[R-1][C-1] != 0:
            for c in range(C):
                if matrix[R-1][c] == 0:
                    matrix[R-1][C-1] = 0
                    break

        #check last col for 0s
        if matrix[R-1][C-1] != 0:
            for r in range(R):
                if matrix[r][C-1] == 0:
                    matrix[R-1][C-1] = 0
                    break
   
        
        #search rows
        for r in range(R - 1):       #2nd last   
            for c in range(C):
                if matrix[r][c] == 0:
                    matrix[r][C-1] = 0 #set last digit of row to 0
                    break
        #search cols
        for c in range(C - 1):      #2nd last 
            for r in range(R):
                if matrix[r][c] == 0:
                    matrix[R-1][c] = 0 #set last digit of col to 0
                    break
        
        #set zeroes for rows
        for r in range(0,R - 1): #until 2nd last digit, where last digit is R-1
            if matrix[r][C-1] == 0:
                for i in range(C):
                    matrix[r][i] = 0


        #set zeroes for col            
        for c in range(0,C - 1): #until 2nd last digit
            if matrix[R-1][c] == 0:
                for i in range(R):
                    matrix[i][c] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)
            
