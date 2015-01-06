class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i=0
        j=0
        while j<len(A):
            if A[j]==elem:
                j+=1
            else:
                if i!=j:
                    A[i]=A[j]
                i+=1
                j+=1
        return i

s = Solution()
data = [([1,2,3],1), ([1,1,2,3],1), ([1,2,3],0),([1,2,2,3],2)]
for d in data:
    print d,d[0][0:s.removeElement(d[0],d[1])]