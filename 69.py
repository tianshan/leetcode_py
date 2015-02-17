class Solution:
    # @param x, an integer
    # @return an integer
    # binarySearch
    def sqrt(self, x):
        l = 0
        r = x
        ans = 0
        while l<=r:
            mid = (l+r)>>1
            t = mid*mid
            if t<x:
                l = mid+1
                ans = mid
            elif t>x:
                r = mid-1
            else:
                return mid
        return ans

class Solution2:
    # @param x, an integer
    # @return an integer
    # newton method
    def sqrt(self, x):
        i=1.0
        while True:
            j=(i+x/i)/2.0
            if(abs(i-j)< 0.000000000005):
                break
            i=j;
        return int(j)

class Solution3:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        return int(x**0.5)

class Solution4:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        ans = 0
        bit = 1<<16
        while bit>0:
            ans = ans | bit
            if ans*ans>x:
                ans = ans ^ bit
            bit = bit>>1
        return int(ans)


s = Solution()
s2 = Solution3()

import time
times = 20

start = time.clock()
for i in range(times):
    s.sqrt(i)
print time.clock()-start

start = time.clock()
for i in range(times):
    s2.sqrt(i)
print time.clock()-start