class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.s = s
        self.do([], 0, 0)
        return self.res

    def do(self, ans, off, i):
        if i==3:
            if off >= len(self.s): return
            if self.s[off]=='0' and len(self.s[off:])>1:return
            a = int(self.s[off:])
            if a<=255:
                ans.append(str(a))
                self.res.append(".".join(ans))
                del ans[-1]
            return
        if off<len(self.s) and self.s[off] == '0':
            ans.append('0')
            self.do(ans, off+1, i+1)
            del ans[-1]
            return
        for j in range(3):
            if off+j+1 >= len(self.s):
                break
            a = int(self.s[off:off+j+1])
            if a>255: break
            ans.append(str(a))
            self.do(ans, off+j+1, i+1)
            del ans[-1]

for d in ["25525511135", "0000", "00011", "", "0", "255255255255"]:
    print Solution().restoreIpAddresses(d)