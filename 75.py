class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = len(A)
        num = [0,0,0]
        i = 0
        while i<n:
            if A[i]==0:
                A[num[0]] = 0
                if num[1]!=0:
                    A[num[0]+num[1]]=1
                if num[2]!=0:
                    A[num[0]+num[1]+num[2]]=2
                num[0] += 1
            elif A[i]==1:
                if num[2]!=0:
                    A[num[0]+num[1]] = 1
                    A[num[0]+num[1]+num[2]]=2
                num[1] += 1
            else:
                num[2] += 1
            i += 1

class Solution2:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        l = 0
        r = len(A)-1
        i = 0
        while i<=r:
            while A[i]==2 and i<r:
                A[i],A[r] = A[r],A[i]
                r -= 1
            while A[i]==0 and i>l:
                A[i],A[l] = A[l],A[i]
                l += 1
            i += 1


s = Solution()
s2 = Solution2()
data = [[1,1,2,0], [1,1,1],[2,2,2],[0,0,0],[1,0]]
for d in data:
    print d,
    s2.sortColors(d)
    print d

# import time
# times = 100

# start = time.clock()
# for i in range(times):
#     for d in data:
#         s.sortColors(d)
# print time.clock()-start

# start = time.clock()
# for i in range(times):
#     for d in data:
#         s2.sortColors(d)
# print time.clock()-start