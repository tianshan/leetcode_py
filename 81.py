class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        off = 0
        if n>1:
            l = 0
            r = n-2
            t = A[n-1]
            while l<r:
                mid = (l+r)/2
                if A[mid]>=t:
                    l = mid+1
                else:
                    r = mid-1
            if l!=0:
                off = l+1
        return off

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
        

if __name__=='__main__':
    s = Solution()
    data = [
            ([1,1], -1),
            ([1,1,2], -1),
            ([1,1,2,1], 0),
            ([1,2,1,1], 0),
            ([2,1,1,1], 0),
            ([2,2,1,1], 0),

            ([0, 1, 2, 4, 5, 6, 7], -1),
            ([6, 7, 0, 1, 2, 4, 5], -1),
            ([3,5,1], 5),
            ([0,1,2], -1),
            ([1,2,0], -1),
            ([2,0,1], -1),
            ([2,1], -1),
            ([4,1,2,3], -1)
            ]
    for d in data:
        print d,s.search(d[0], d[1])
