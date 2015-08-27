class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        if n==0:
            return -1
        if n==1:
            ri = 0
        else:
            ri = self.searchBig(A, A[n-1], 0, n-1)
        return self.binarySearch(A, target, ri, 0, n)

    def searchBig(self, A, target, l, r):
        if r-l<=1:
            if A[l]>A[l+1]:
                return l+1
            else:
                return 0
        mid = (l+r)/2
        if A[mid]>target:
            return self.searchBig(A, target, mid, r)
        else:
            return self.searchBig(A, target, l, mid)

    def binarySearch(self, A, target, ri, l, r):
        if r==l:
            i = (l+ri)%len(A)
            if A[i]==target:
                return i
            else:
                return -1
        mid = (l+r)/2
        if A[(mid+ri)%len(A)]<target:
            return self.binarySearch(A, target, ri, mid+1, r)
        if A[(mid+ri)%len(A)]>target:
            return self.binarySearch(A, target, ri, l, mid)
        return (mid+ri)%len(A)

class Solution2:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        l = 0
        r = n-1
        while l<r:
            mid = (l+r)/2
            if A[mid]>A[r]:
                l = mid+1
            else:
                r = mid
        off = l

        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)/2
            if A[(mid+off)%n]<target:
                l = mid+1
            elif A[(mid+off)%n]>target:
                r = mid-1
            else:
                return (mid+off)%n
        return -1

class Solution3:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) / 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[r] >= nums[mid]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__=='__main__':
    data = [
            ([1], 0),
            ([0, 1, 2, 4, 5, 6, 7], -1),
            ([6, 7, 0, 1, 2, 4, 5], -1),
            ([3,5,1], 5),
            ([1,2,3,4,5,6,7,8], 4),
            ([0,1,2,4,5,6,7],4),
            ([1,2,4,5,6,7,0],4),
            ([2,4,5,6,7,0,1],-1),
            ([4,5,6,7,0,1,2],-1),
            ([5,6,7,0,1,2,4],-1),
            ([6,7,0,1,2,4,5],-1),
            ([7,0,1,2,4,5,6],-1),
            ([1], -1),
            ([1,2], -1),
            ([0,1,2], -1),
            ([1,2,0], -1),
            ([2,0,1], -1),
            ([2,1], -1),
            ([4,1,2,3], -1)
            ]
    for d in data:
        print d,Solution2().search(d[0], d[1])
