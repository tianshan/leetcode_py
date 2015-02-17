class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        i = 0
        while i<(n/2):
            for j in range(i, n-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = temp
            i += 1
        return matrix

s = Solution()
data = [[[]], [[1]], [[1,2],[3,4]], [[1,2,3],[4,5,6],[7,8,9]], [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]
for d in data:
    s.rotate(d)
    for r in d:
        print r
    print ''