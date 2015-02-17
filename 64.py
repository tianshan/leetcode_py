class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==0 and j!=0:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
                elif j==0 and i!=0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                elif i!=0 and j!=0:
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j])+grid[i][j]
        return grid[n-1][m-1]

s = Solution()
data = [[1,1,2],
        [2,1,3],
        [1,2,1]]
print s.minPathSum(data)
