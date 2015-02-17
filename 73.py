class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    # space O(m+n)
    def setZeroes(self, matrix):
        n = len(matrix)
        if n==0:
            return matrix 
        m = len(matrix[0])

        rows = [False for i in range(n)]
        cols = [False for i in range(m)]

        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    rows[i] = True
                    cols[j] = True

        for i in range(n):
            if rows[i]:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(m):
            if cols[j]:
                for i in range(n):
                    matrix[i][j] = 0

class Solution2:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    # space O(m+n)
    def setZeroes(self, matrix):
        n = len(matrix)
        if n==0:
            return matrix 
        m = len(matrix[0])

        row = None
        col = None
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    if row==None:
                        row = i 
                        col = j
                    matrix[row][j] = 0
                    matrix[i][col] = 0
        print row, col
        if row!=None:
            for i in range(n):
                if i==row:
                    continue 
                if not matrix[i][col]:
                    for j in range(m):
                        matrix[i][j] = 0
            for j in range(m):
                if not matrix[row][j]:
                    for i in range(n):
                        matrix[i][j] = 0
                matrix[row][j] = 0



s = Solution2()
data = [[1,2,3],[1,0,1]]
data = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
for d in data:
    print d
s.setZeroes(data)
for d in data:
    print d