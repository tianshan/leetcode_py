class Solution:
    # @return a string
    def countAndSay(self, n):
        ans = '1'
        for i in range(1, n):
            last = ans[0]
            num = 1
            temp = ''
            for j in range(1, len(ans)):
                if ans[j]==last:
                    num += 1
                else:
                    temp += str(num)+last
                    last = ans[j]
                    num = 1
            ans = temp+str(num)+last
        return ans

if __name__=='__main__':
    s = Solution()
    for i in range(1,20):
        print s.countAndSay(i)