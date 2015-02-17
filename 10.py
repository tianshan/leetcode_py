class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        return self.match(s, p)

    def match(self, s, p):
        if len(s)==0:
            if len(p)==0:
                return True
            else:
                return False
        if len(p)==0:
            if len(s)==0:
                return True
            else:
                return False
        if len(p)==1:
            if len(s)>1 or s[0]!=p[0]:
                return False
            return True
        if p[1]!='*':
            if p[0]=='.' or p[0]==s[0]:
                return self.match(s[1:], p[1:])
            return True
        ans = self.match(s, p[2:])
        for i in range(len(s)):
            if p[0]=='.' or p[0]==s[i]:
                ans = ans or self.match(s[i+1:], p[2:])
            else:
                break
        return ans


if __name__=='__main__':
    s = Solution()
    data = [('aa', 'a'), ('aa','aa'), ('aaa','aa'),
            ('aa','a*'), ('aa','.*'), ('ab', '.*'), ('aab', 'c*a*b'),
            ('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')]
    # for d in data:
    #     print d,s.isMatch(d[0], d[1])
    import re
    for d in data:
        pattern = re.compile(d[1])
        match = pattern.match(d[0])
        if match and match.group()==d[0]:
            print d,True
        else:
            print d,False