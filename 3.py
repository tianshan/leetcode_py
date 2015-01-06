class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        index = dict()
        start = 0
        max_len = 0
        for i,ss in enumerate(s):
            k = index.get(ss, -1)
            if k>=start:
                max_len = max(max_len, i-start)
                start = k+1
            index[ss] = i
            if i==len(s)-1:
                max_len = max(max_len, i-start+1)
        return max_len


if __name__=='__main__':
    s = Solution()
    data_in = ['abcabcbb', 'bbbb', 'ababc', 'b', 'ababcabca']
    for d in data_in:
        print s.lengthOfLongestSubstring(d)