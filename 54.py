class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        n = len(matrix)
        if n==0:
            return []
        m = len(matrix[0])
        i = 0
        ans = []
        idx = 0
        while i<n and i<m:
            if n-i==1:
                for j in range(i, m):
                    ans.append(matrix[i][j])
            elif m-i==1:
                for j in range(i, n):
                    ans.append(matrix[j][i])
            else:
                for j in range(i, m):
                    ans.append(matrix[i][j])
                for j in range(i+1, n-1):
                    ans.append(matrix[j][m-1])
                for j in range(m-1, i-1, -1):
                    ans.append(matrix[n-1][j])
                for j in range(n-2, i, -1):
                    ans.append(matrix[j][i])
            i += 1
            n -= 1
            m -= 1
        return ans

s = Solution()
data = [ [[1,2,3],[4,5,6],[7,8,9]],
        [[1]],
        [[1,2,3]],
        [[1,2,3],[4,5,6]],
        [[1,2],[3,4],[5,6]],
        [],
        [[3],[2]],
        [[7],[9],[6]]
        ]
for d in data:
    print s.spiralOrder(d)