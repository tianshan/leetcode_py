class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n==0:
            return 0
        if n<2:
            return 1
        a = 1
        b = 2
        for i in range(3, n+1):
            temp = b
            b = a+b
            a = temp
        return b

import math

class Solution2:
    # when n>=71, the float will be imprecision
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a = math.sqrt(5)
        ans = a/5/math.pow(2,n)*(math.pow(a+1, n)-math.pow(1-a, n))
        return int(ans)


s = Solution()
s2 = Solution2()
for d in range(1, 100):
    a = s.climbStairs(d)
    b = s2.climbStairs(d+1)
    if a!=b:
        print d,a,b