class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        vis = [0 for i in range(size+2)]
        for n in nums:
            if n >= 0 and n<=size:
                vis[n] = 1
        for i in xrange(1, size+2):
            if vis[i] == 0:
                return i

class Solution2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        for i in xrange(size):
            if nums[i] == i+1: continue
            x = nums[i]
            while nums[i]<=size and nums[i]>0 and nums[i] != nums[x-1]:
                x = nums[x-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = x
        for i in xrange(size):
            if nums[i] != i+1:
                return i+1
        return size+1


data = [1,2,3,4]
# data = [1,2,3,5]
# data = [1,1]
# data = [3,4,-1,1]
# data = [2,1]
print Solution2().firstMissingPositive(data)