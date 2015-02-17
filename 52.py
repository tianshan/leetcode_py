class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.n = n
        self.res = 0
        self.maxn = (1<<n)-1
        self.findQueens(0, 0, 0, 0)
        return self.res

    def findQueens(self, k, row, ld, rd):
        if k==self.n and self.n>0:
            self.res += 1
            return
        pos = self.maxn & ~(row | ld | rd)
        for i in range(self.n):
            t = 1<<i
            if pos & t:
                self.findQueens(k+1, row|t, (ld+t)<<1, (rd+t)>>1)
                pos = pos | t



s = Solution()
for i in range(11):
    print s.totalNQueens(i)