class Solution:
    # @param A, a list of integers
    # @return an integer
    # O(n^2)
    def trap(self, A):
        if len(A)<=1:
            return 0
        lb = [-1 for i in range(len(A))]
        ans = 0
        for i in range(1, len(A)):
            if A[i]<=A[i-1]:
                lb[i] = i-1
            else:
                j = i-1
                temp_sum = 0
                while j>=0 and A[j]<A[i]:
                    if lb[j]!=-1:
                        temp_sum += A[j]*(j-lb[j])
                    else:
                        temp_sum = A[j]*(i-j-1)-temp_sum
                    j = lb[j]
                if j!=-1:
                    lb[i] = j
                    ans += A[i]*(i-1-j)-temp_sum
                elif lb[i-1]!=-1:
                    ans += temp_sum
        return ans
        
class Solution2:
    # @param A, a list of integers
    # @return an integer
    # O(n^2)
    def trap(self, A):
        if len(A)<=1:
            return 0
        maxh = A[0]
        maxi = 0
        tsum = 0
        ans = 0
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                minh = min(A[i], maxh)
                ans += minh*(i-1-maxi)-tsum
                if A[i]>=maxh:
                    maxh = A[i]
                    maxi = i
                else:
                    tsum = minh*(i-maxi)
            else:
                tsum += A[i]
        return ans

class Solution3:
    # @param A, a list of integers
    # @return an integer
    # O(n^2)
    def trap(self, A):
        n = len(A)
        if n<=2:
            return 0
        l = 0
        r = n-1
        while l<(n-1) and A[l]<=A[l+1]:
            l += 1
        while r>0 and A[r]<=A[r-1]:
            r -= 1
        maxl = A[l]
        maxr = A[r]
        ans = 0
        while l<r:
            if maxl<maxr:
                l += 1
                if A[l]<=maxl:
                    ans += maxl-A[l]
                else:
                    maxl = A[l]
            else:
                r -= 1 
                if A[r]<=maxr:
                    ans += maxr-A[r]
                else:
                    maxr = A[r]
        return ans




s = Solution3()
s2 = Solution()
data = [
        [1,0,1],
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [3,2,1],
        [2,0,1,0,2],
        [3,2,1,0,1]
        ]
# for d in data:
#     print d,s.trap(d)

import time
import random
times = 1

d = []
for i in range(1000):
    d.append(int(random.random()*1000))



start = time.clock()
for i in range(times):
    # for d in data:
    print s.trap(d)
print time.clock()-start

start = time.clock()
for i in range(times):
    # for d in data:
    print s2.trap(d)
print time.clock()-start