class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        candidates.sort()
        ans = self.dfs(candidates, target, 0)
        return ans

    def dfs(self, nums, target, idx):
        if idx>=len(nums) or target-nums[idx]<0:
            return []
        if target-nums[idx]==0:
            return [[nums[idx]]]
        else:
            ans = []
            temp = []
            while target>0:
                ans += [temp+x for x in self.dfs(nums, target, idx+1)]
                target -= nums[idx]
                temp.append(nums[idx])
                if target==0:
                    ans.append(temp)
            return ans

# class Solution2:
#     # @param candidates, a list of integers
#     # @param target, integer
#     # @return a list of lists of integers
#     def combinationSum(self, candidates, target):
#         candidates = list(set(candidates))
#         candidates.sort()
#         return self.dfs(candidates, target, 0, 0)

#     def dfs(self, nums, target, idx, p):
#         if idx>=len(nums) or target<0:
#             return []
#         ans = self.dfs(nums, target, idx+1, 0)
#         temp = target - nums[idx]*(1<<p)
#         if temp==0:
#             ans += [[nums[idx] for i in range(1<<p)]]
#         elif temp>0:
#             ans += self.dfs(nums, target, idx, p+1)
#             res = self.dfs(nums, temp, idx, p+1)
#             res += self.dfs(nums, temp, idx+1, 0)
#             if res:
#                 ans += [[nums[idx] for i in range(1<<p)]+x for x in res]
#         return ans

if __name__=='__main__':
    s = Solution()
    data = [([2,3,6,7],7), ([2,3], 1), ([1,2,3], 6), ([2],1)]
    for d in data:
        print s.combinationSum(d[0], d[1])


