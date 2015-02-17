class Solution:
    # @return an integer
    def maxArea(self, height):
        ans = 0
        j = len(height)-1
        i = 0
        while i<j:
            ans = max(ans, (j-i)*min(height[j], height[i]))
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return ans

if __name__=='__main__':
    s = Solution()
    data = [[1,2,3,4], [1,2,3,1]]
    for d in data:
        print d,s.maxArea(d)