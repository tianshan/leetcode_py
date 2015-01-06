class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        ans = ['']
        for d in str(digits):
            t = self.getLetter(d)
            if t==-1:
                continue
            ans = [x+y for x in ans for y in t]
        return ans

    def getLetter(self, d):
        if d=='2':
            return 'abc'
        if d=='3':
            return 'def'
        if d=='4':
            return 'ghi'
        if d=='5':
            return 'jkl'
        if d=='6':
            return 'mno'
        if d=='7':
            return 'pqrs'
        if d=='8':
            return 'tuv'
        if d=='9':
            return 'wxyz'
        if d=='0':
            return ' '
        return -1

if __name__=='__main__':
    s = Solution()
    data = [23, 12, 209, 1234]
    for d in data:
        print s.letterCombinations(d)