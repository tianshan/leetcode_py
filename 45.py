class Solution:
    # O(n^2)
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        steps = [n+1 for i in range(n)]
        steps[0] = 0
        for i in range(n-1):
            if steps[i]==n+1:
                return -1
            for j in range(A[i]+1):
                if i+j>=n:
                    break
                steps[i+j] = min(steps[i]+1, steps[i+j])
        return steps[n-1]

class Solution2:
    # O(n)
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A)<=1:
            return 0
        maxn = 0
        ans = 0
        i = 0
        while i<=maxn:
            temp = 0
            while i<=maxn:
                if i+A[i]>temp:
                    temp = i+A[i]
                i += 1
            if temp==maxn:
                return -1
            ans += 1
            if temp>=len(A)-1:
                return ans
            i = maxn+1
            maxn = temp


s = Solution2()
# data = [[2,3,1,1,4],[2,1],[1,2,3]]
# for d in data:
#     print s.jump(d)
d = []
for i in range(25000, -1, -1):
    d.append(i)
print s.jump(d)