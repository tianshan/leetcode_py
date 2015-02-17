class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        ans = [[0 for j in range(m)] for i in range(n)]
        if obstacleGrid[0][0]!=1:
            ans[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[i][0]!=1:
                ans[i][0] = ans[i-1][0]
        for j in range(1, m):
            if obstacleGrid[0][j]!=1:
                ans[0][j] = ans[0][j-1]
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]!=1:
                    ans[i][j] = ans[i][j-1]+ans[i-1][j]
        return ans[n-1][m-1]

s = Solution()
data = [[0]]
print s.uniquePathsWithObstacles(data)


