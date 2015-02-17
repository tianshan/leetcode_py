class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ans = [[0 for i in range(n)] for i in range(n)]
        i = 0
        idx = 1
        while i<n:
            if n-i==1:
                for j in range(i, n):
                    ans[i][j] = idx
                    idx += 1
            else:
                for j in range(i, n):
                    ans[i][j] = idx
                    idx += 1
                for j in range(i+1, n-1):
                    ans[j][n-1] = idx
                    idx += 1
                for j in range(n-1, i-1, -1):
                    ans[n-1][j] = idx
                    idx += 1
                for j in range(n-2, i, -1):
                    ans[j][i] = idx
                    idx += 1
            i += 1
            n -= 1
        return ans

s = Solution()
for i in [0,1,2,3,4]:
    print s.generateMatrix(i)