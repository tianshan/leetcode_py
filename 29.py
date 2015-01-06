class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        max_int = 2147483647
        min_int = -2147483648
        if divisor==0 \
            or (dividend>max_int) or (dividend<min_int) \
            or (divisor>max_int) or (divisor<min_int):
            return max_int

        d1 = abs(dividend)
        d2 = abs(divisor)

        table = [(d2,1)]
        x = d2
        n = 1
        while x+x<=max_int+1:
            x = x+x
            n = n+n
            table.append((x,n))

        ans = 0
        for i in range(1, len(table)+1):
            if d1>=table[-i][0]:
                d1 -= table[-i][0]
                ans += table[-i][1]

        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            ans = -ans
        if ans>max_int:
            return max_int
        if ans<min_int:
            return min_int
        return ans
        

if __name__=='__main__':
    s = Solution()
    data = [(-1,2), (1,-2), (4,2), (-3, 2), (3,-2), (3,2),(-2147483648, -1),(-2147483648, 1)]
    for d in data:
        print d,s.divide(d[0], d[1])