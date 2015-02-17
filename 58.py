class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s_len = len(s)
        if s_len<1:
            return 0
        index = 1
        while index<=s_len and s[-index]==' ':
            index += 1
        ans = 0
        for i in range(index, s_len+1):
            if s[-i]==' ':
                break
            ans += 1
        return ans

if __name__=='__main__':
    s = Solution()
    data = ['hello world','   ','','hello', 'a ']
    for d in data:
        print d,s.lengthOfLastWord(d)