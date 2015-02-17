class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n<0:
            x = 1.0/x
            n = -n
        ans = 1.0
        while n>0:
            if n&1 == 1:
                ans *= x
            x *= x
            n = n>>1
        return float(ans)

if __name__=='__main__':
    s = Solution()
    data = [(1,2), (2,10), (3,10), (2,5), (1.1, 3), (34.00515, -3)]
    for d in data:
        a = s.pow(d[0], d[1])
        print a, type(a)