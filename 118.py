class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        res = [[1]]
        for i in xrange(1, numRows):
            tmp = [1]
            size = len(res[-1])-1
            for j in xrange(size):
                tmp.append(res[-1][j]+res[-1][j+1])
            tmp.append(1)
            res.append(tmp)
        return res 

res = Solution().generate(5)
for r in res:
    print r