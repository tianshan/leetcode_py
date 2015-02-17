class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        n = len(S)
        m = 1<<n
        ans = []
        S.sort()
        for i in range(m):
            temp = []
            for j in range(n):
                if i&(1<<j)>0:
                    temp.append(S[j])
            ans.append(temp)
        return ans 

s = Solution()
print s.subsets([1])