class Solution:
    # @return an integer
    # fast C(n, k), O(k)
    def uniquePaths(self, m, n):
        return self.combination(n+m-2, n-1)

    def combination(self, n, k):
        res = 1 
        if n-k>k:
            k = n-k
        for i in range(k):
            if res%(i+1)==0:
                res /= i+1
                res *= n-i 
            elif (n-i)%(i+1)==0:
                res *= (n-i)/(i+1)
            else:
                g = self.gcd(res, i+1)
                res /= g 
                res *= (n-i) / ((i+1)/g)
        return res

    def gcd(self, a, b):
        while b!=0:
            t = b
            b = a%b
            a = t
        return a




s = Solution()
data = [(1,1),(2,2),(3,7), (3,3), (100,100)]
for d in data:
    print s.uniquePaths(d[0], d[1])