class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = 0
        res = [0]
        while len(res)>size:
            size += 1
            for i in range(0, n):
                ans = res[-1] ^ (1 << i)
                if ans not in res:
                    res.append(ans)
                    break
        return res


    def do2(self, x, k):
        for i in range(k, self.n):
            ans = x ^ (1<<i)
            if ans in self.res: continue
            self.res.append(ans)
            print bin(ans)[2:].zfill(3),x,i
            self.do(ans, k+1)

    def grayCode2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = 0
        res = [0]
        for i in range(0, n):
            size = len(res)
            v = 1<<i
            while size>0:
                size -= 1
                res.append(res[size] | v)
                print v,res[-1]
            print ''
        return res

import time
n = 3
# start = time.time()
# ret = Solution().grayCode(n)
# # print ret
# print time.time()-start

start = time.time()
ret = Solution().grayCode2(n)
print ret
print time.time()-start




