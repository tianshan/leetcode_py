class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r and l<len(nums) and r >= 0:
            mid = (l+r) / 2
            if nums[mid] == target:
                return True
            elif nums[l] == nums[mid]:
                l += 1
            elif nums[r] == nums[mid]:
                r -= 1
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
        

if __name__=='__main__':
    s = Solution()
    data = [
            ([1,1], -1),
            ([1,1,2], -1),
            ([1,1,2,1], 0),
            ([1,2,1,1], 0),
            ([2,1,1,1], 0),
            ([2,2,1,1], 0),

            ([0, 1, 2, 4, 5, 6, 7], -1),
            ([6, 7, 0, 1, 2, 4, 5], -1),
            ([3,5,1], 5),
            ([0,1,2], -1),
            ([1,2,0], -1),
            ([2,0,1], -1),
            ([2,1], -1),
            ([4,1,2,3], -1),
            ([1,1,3,1], 3)
            ]
    for d in data:
        print d,s.search(d[0], d[1])
