class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in xrange(0, rowIndex):
            if i > rowIndex/2:
                tmp = res[rowIndex-i-1]
            else:
                tmp = res[-1] * (rowIndex-i) / (i+1)
            res.append(tmp)
        return res

print Solution().getRow(6)