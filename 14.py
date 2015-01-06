class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        ans = ''
        for i in range(len(strs[0])):
            x = strs[0][i]
            for s in strs:
                if i>=len(s) or s[i]!=x:
                    return ans
            ans += x
        return ans

if __name__=='__main__':
    s = Solution()
    strs = []
    print s.longestCommonPrefix(strs)
