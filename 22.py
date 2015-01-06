class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return self.gen(n,0)

    def gen(self, l, r):
        if l==0:
            return [')'*r]
        ans = ['('+x for x in self.gen(l-1,r+1)]
        if r>0:
            ans += [')'+x for x in self.gen(l,r-1)]
        return ans

if __name__=='__main__':
    s = Solution()
    data = [0,1,2,3]
    for d in data:
        print s.generateParenthesis(d)