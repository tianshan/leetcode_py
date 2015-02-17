class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        last = None
        ans = 0
        twice = True
        for d in A:
            if last==None or (last!=None and d!=last):
                A[ans] = d
                ans += 1
                last = d
                twice = True
            elif twice:
                A[ans] = d
                ans += 1
                twice = False
        return ans

s = Solution()
data = [[1,1,1,2,2,3],[1,1,1,1],[1,1,1,2,2,2]]
for d in data:
    l = s.removeDuplicates(d)
    print d[:l]

