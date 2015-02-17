class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        na = len(a)
        nb = len(b)
        i = 1
        j = 1
        ans = ''
        r = 0
        while i<=na or j<=nb or r>0:
            temp = r
            if i<=na and a[-i]=='1':
                temp += 1
            if j<=nb and b[-i]=='1':
                temp += 1
            r = temp>>1
            if temp&1==1:
                ans += '1'
            else:
                ans += '0'
            i += 1
            j += 1
        return ans[::-1]

s = Solution()
data = [('11','11'), ('0','0'), ('10000','10000')]
for d in data:
    print s.addBinary(d[0], d[1])