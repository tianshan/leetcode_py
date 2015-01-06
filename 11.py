class Solution:
    # @return an integer
    def maxArea(self, height):
        maxa = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                maxa = max(maxa, (j-i)*min(height[i], height[j]))
        return maxa


if __name__=="__main__":
    s = Solution()
    data = [[2,2,3], [0,0,0], [2,3,2]]
    for d in data:
        print s.maxArea(d)