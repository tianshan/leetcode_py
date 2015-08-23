class Solution(object):
    # Catalan Number  (2n)!/((n+1)!*n!)  
    # h(n) = h(0)*h(n-1)+h(1)*h(n-2)...
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        res[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]




# print Solution().numTrees(3)


a = [0] * 3
a[0] = 1
print a