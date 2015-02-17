class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # candidates = list(set(candidates))
        candidates.sort()
        ans = self.dfs(candidates, target, 0, True)
        return ans

    def dfs(self, nums, target, idx, isRepeatable):
        if idx>=len(nums) or target-nums[idx]<0:
            return []
        if target-nums[idx]==0:
            return [[nums[idx]]]

        ans = self.dfs(nums, target, idx+1, False)
        if idx>0 and nums[idx]==nums[idx-1]:
            if isRepeatable:
                ans += [[nums[idx]]+x for x in self.dfs(nums, target-nums[idx], idx+1, True)]
        else:
            ans += [[nums[idx]]+x for x in self.dfs(nums, target-nums[idx], idx+1, True)]
        return ans

if __name__=='__main__':
    s = Solution()
    data = [([2,3,6,7],7), ([2,3], 1), ([1,2,3], 6), ([2],1),
            ([10,1,2,7,6,1,5], 8),
            ([1,1,1,1,1,1,2,3], 6)]
    for d in data:
        print s.combinationSum(d[0], d[1])