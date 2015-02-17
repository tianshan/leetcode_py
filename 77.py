import itertools

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        nums = [i for i in range(1, n+1)]
        ans = [list(x) for x in itertools.combinations(nums, k)]
        return ans

class Solution2:
    # @return a list of lists of integers
    def combine(self, n, k):
        results = [[i] for i in range(n-k+1)]
        for p in range(1, k):
            results = [r+[x] for r in results for x in range(r[-1]+1, n-k+p+1)]
        return [[x+1 for x in r] for r in results]

s = Solution()
s2 = Solution2()

import time
times = 100

start = time.clock()
for i in range(times):
    s.combine(10,5)
print time.clock()-start

start = time.clock()
for i in range(times):
    s2.combine(10,5)
print time.clock()-start