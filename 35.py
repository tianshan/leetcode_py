class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        ans = self.binarySearch(A, 0, len(A), target)
        if ans<0:
            return 0
        return ans

    def binarySearch(self, A, l, r, target):
        mid = (l+r)/2
        if mid==l:
            if target==A[mid]:
                return mid
            elif target<A[mid]:
                return mid-1
            else:
                return mid+1
        if target<A[mid]:
            return self.binarySearch(A, l, mid, target)
        else:
            return self.binarySearch(A, mid, r, target)

if __name__=='__main__':
    s = Solution()
    data = [([1,3,5,6],1),([1,3,5,6],3),([1,3,5,6],5),([1,3,5,6],6),([0],-1),([0],0),([0],1)]
    for d in data:
        print d,s.searchInsert(d[0], d[1])