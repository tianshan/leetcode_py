class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = self.binarySearch(A, 0, len(A), target, 0)
        if left<0 or left>=len(A) or A[left]!=target:
            return [-1,-1]
        right = self.binarySearch(A, 0, len(A), target, 1)
        return [left, right]

    def binarySearch(self, A, l, r, target, lr):
        mid = (l+r)/2
        if mid==l:
            if target==A[mid]:
                return mid
            elif target<A[mid]:
                return mid-1
            else:
                return mid+1
        if target<A[mid] or (target==A[mid] and lr==0):
            return self.binarySearch(A, l, mid, target, lr)
        elif target>A[mid] or (target==A[mid] and lr==1):
            return self.binarySearch(A, mid, r, target, lr)

if __name__=='__main__':
    s = Solution()
    data = [([5,7,7,8,8,10],8), ([5,7,7,8,8,10],5), 
            ([5,7,7,8,8,10],6), ([0],0), ([0],1),
            ([5,7,7,8,8,10],10),
            ([5,7,7,8,8,10],11)]
    for d in data:
        print d,s.searchRange(d[0], d[1])