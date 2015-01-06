class Solution:
    # @return an integer
    def romanToInt(self, s):
        ans = 0
        last = 0
        for i in range(len(s)):
            a = self.getNum(s[-1-i])
            if a>=last:
                ans += a 
            else:
                ans -= a
            last = a
        return ans
    def getNum(self, c):
        if c=='I':
            return 1
        if c=='V':
            return 5
        if c=='X':
            return 10
        if c=='L':
            return 50
        if c=='C':
            return 100
        if c=='D':
            return 500
        if c=='M':
            return 1000
    def test1(self, s):
        ans = 0
        for i in range(1,len(s)):
            ans += 1
    def test2(self, s):
        ans = 0
        s_len = len(s)
        for i in range(1, s_len):
            ans += 1

if __name__=='__main__':
    data = ['I', 'II', 'IV', 'IX', 'X', 'XI', 'XIV', 'XV']
    s = Solution()
    for d in data:
        print d,s.romanToInt(d)
    # while 1:
    #     d = raw_input()
    #     print s.romanToInt(d)
    # import time
    # times = 10000
    # data = data*times
    # start = time.clock()
    # s.test1(data)
    # end = time.clock()
    # print end-start
    # start = end 
    # s.test2(data)
    # print time.clock()-start
