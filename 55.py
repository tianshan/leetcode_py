class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A)==0:
            return False
        if len(A)==1:
            return True
        vis = [False for x in range(len(A))]
        vis[0] = True
        maxn = 0
        ans = False
        for i in range(len(A)-1):
            if vis[i]==False:
                continue
            if i+A[i]<=maxn:
                continue
            maxn = i+A[i]
            if maxn>=len(A)-1:
                ans = True
                break
            for j in range(A[i]):
                vis[i+1+j] = True
        return ans

class Solution2:
    # O(n)
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A)==1:
            return True
        if A[0]==0:
            return False
        for i in range(1, len(A)-1):
            A[i] = max(A[i], A[i-1]-1)
            if A[i]==0:
                return False
        return True

s = Solution2()
data = [[2,3,1,1,4],[3,2,1,0,4],[0],[0,2,3]]
for d in data:
    print s.canJump(d)