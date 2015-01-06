class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)<=1:
            return len(A)
        i=1
        j=1
        last=A[0]
        while j<len(A):
            if A[j]==last:
                j+=1
            else:
                last=A[j]
                if i!=j:
                    A[i]=A[j]
                i+=1
                j+=1
        return i

s = Solution()
data = [[1,1,2],[1],[],[1,2],[1,2,2,2],[1,2,2,3,3],[1,1,2,2,3,3,3]]
for d in data:
    print d,d[0:s.removeDuplicates(d)]