class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows==1:
            return s
        s_len = len(s)
        g = (s_len-1)/(nRows-1)+1
        ans = ''
        for i in range(nRows):
            for j in range(1, g+1):
                if i%(nRows-1)==0:
                    x = i+2*(j-1)*(nRows-1)
                else:
                    if j%2==0:
                        x = (nRows-1)*j-i
                    else:
                        x = (nRows-1)*(j-1)+i

                if x>=s_len:
                    break
                ans += s[x]
        return ans

if __name__=="__main__":
    s = Solution()
    for d in [('PAYPALI',3), ('PAYPALISHIRING',3), 
            ('ABCD',2), ('AB',2),
            ('PAYPALISHIRI',3),
            ('ABCD',1)]:
        print s.convert(d[0], d[1])