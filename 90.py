class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        m = 1<<n
        ans = set()
        nums.sort()
        for i in range(m):
            temp = []
            for j in range(n):
                if i&(1<<j)>0:
                    temp.append(nums[j])
            ans.add(tuple(temp))
        return list([list(x) for x in ans])

class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.nums = sorted(nums)
        self.n = len(nums)
        self.do([], 0)
        return self.res

    def do(self, path, begin):
        self.res.append(path[:])
        for i in xrange(begin, self.n):
            if i == begin or self.nums[i] != self.nums[i-1]:
                path.append(self.nums[i])
                self.do(path, i+1)
                del path[-1]

import time

data = [1,2,2,3,3,4,4]

start = time.time()
Solution().subsetsWithDup(data) 
print (time.time()-start)*1000

start = time.time()
Solution2().subsetsWithDup(data) 
print (time.time()-start)*1000


