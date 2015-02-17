class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n==0:
            return False
        m = len(matrix[0])
        l = 0
        r = n*m-1
        while l<=r:
            mid = (l+r)>>1
            i = mid/m
            j = mid-i*m
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                l = mid+1
            else:
                r = mid-1
        return False

s = Solution()
data = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print s.searchMatrix(data, 49)

