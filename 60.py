class Solution:
    # @return a string
    def getPermutation(self, n, k):
        temp = 1
        for i in range(1, n):
            temp *= i
        nums = [str(i) for i in range(1,n+1)]
        ans = ''
        for i in range(n-1, 0, -1):
            j = 0
            while k-temp>0:
                k -= temp
                j += 1
            ans += nums[j]
            nums.pop(j)
            temp /= i
        ans += nums[0]
        return ans

s = Solution()
for i in range(1, 3):
    print s.getPermutation(2, i)


