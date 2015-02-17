class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if n==0:
            return
        i = 0
        while i<m:
            if A[i]>B[0]:
                temp = A[i]
                A[i] = B[0]
                j = 1
                while j<n and temp>B[j]:
                    B[j-1] = B[j]
                    j += 1
                B[j-1] = temp
            else:
                i += 1
        j = 0
        while j<n:
            A[i+j]=B[j]
            j += 1

class Solution2:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m-1
        j = n-1
        while j>=0:
            while i>=0 and A[i]>=B[j]:
                A[i+j+1] = A[i]
                i -= 1
            A[i+j+1] = B[j]
            j -= 1

class Solution3:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        while m and n:
            (A[m + n - 1], m, n) = (A[m - 1], m - 1, n) if A[m - 1] > B[n - 1] else (B[n - 1], m, n - 1)
        A[:n] = B[:n]

class Solution4:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        m -= 1
        n -= 1
        num = m+n+1
        while m>=0 and n>=0:
            if A[m]>B[n]:
                A[num] = A[m]
                m -= 1
            else:
                A[num] = B[n]
                n -= 1
            num -= 1
        if n>-1:
            A[:n+1] = B[:n+1]


s = Solution4()
s2 = Solution3()

data = [[[1,2,3],[4,5,6]], 
        [[1,3,5],[2,4,6]], 
        [[1,3,6],[2,4,5]], 
        [[1],[]], [[],[1]], 
        [[],[]]]
# for d in data:
#     l = len(d[0])
#     d[0] += [0 for i in range(len(d[1]))]
#     s.merge(d[0], l, d[1], len(d[1]))
#     print d[0]

import time 
times = 1

start = time.clock()
for i in range(times):
    for d in data:
        l = len(d[0])
        d[0] += [0 for i in range(len(d[1]))]
        s.merge(d[0], l, d[1], len(d[1]))
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        l = len(d[0])
        d[0] += [0 for i in range(len(d[1]))]
        s2.merge(d[0], l, d[1], len(d[1]))
print time.clock()-start