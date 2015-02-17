class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        asum = 0
        maxn = A[0]
        for d in A:
            asum += d
            maxn = max(maxn, asum)
            if asum<0:
                asum = 0
        return maxn

s = Solution()
data = [[-2,1,-3,4,-1,2,1,-5,4],[0],[-3,-2,-1]]
for d in data:
    print s.maxSubArray(d)
