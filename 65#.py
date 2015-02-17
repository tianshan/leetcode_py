import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        pattern = re.compile(
            r'^\s*[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?\s*$')
        match = pattern.match(s)
        if match!=None:
            return True
        else:
            return False


s = Solution()
data = [
        '0', ' 0.1', 'abc', '1 a', '2e10','.1', '   ', 'e9', '1.0e1',
        '3.','3.e1']
for d in data:
    print d,s.isNumber(d)