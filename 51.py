class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        queens = [0 for i in range(n)]
        self.n = n
        self.res = []
        self.maxn = (1<<n)-1
        self.findQueens(0, queens, 0, 0, 0)
        return self.res

    def findQueens(self, k, queens, row, ld, rd):
        if k==self.n and self.n>0:
            self.appendResult(queens)
            return
        pos = self.maxn & ~(row | ld | rd)
        for i in range(self.n):
            t = 1<<i
            if pos & t:
                queens[k] = i
                self.findQueens(k+1, queens, row|t, (ld+t)<<1, (rd+t)>>1)
                pos = pos | t

    def appendResult(self, queens):
        temp = []
        for i in range(self.n):
            t = '.'*(queens[i])+'Q'+'.'*(self.n-queens[i]-1)
            temp.append(t)
        self.res.append(temp)

class Solution2:
    # @return a list of lists of string
    def solveNQueens(self, n):
        queens = [0 for i in range(n)]
        ans = []
        self.findQueens(0, n, queens, ans)
        res = []
        for a in ans:
            temp = []
            for i in range(n):
                t = ['.' for j in range(n)]
                t[a[i]] = 'Q'
                temp.append(''.join(t))
            res.append(temp)
        return res

    def findQueens(self, k, n, queens, ans):
        if k==n and n>0:
            ans.append(queens[:])
            return
        candi = []
        for i in range(n):
            flag = True
            for j in range(k):
                if queens[j]==i:
                    flag = False
                    break
                if (k-j)==abs(queens[j]-i):
                    flag = False
                    break
            if flag:
                candi.append(i)
        for i in candi:
            queens[k] = i
            self.findQueens(k+1, n, queens, ans)

s = Solution()
s2 = Solution2()

# print s.solveNQueens(4)

import time
t = 13

start = time.clock()
s.solveNQueens(t)
print time.clock()-start

# start = time.clock()
# s2.solveNQueens(t)
# print time.clock()-start
