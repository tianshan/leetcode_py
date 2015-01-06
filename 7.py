class Solution:
    # @return an integer
    def reverse(self, x):
        int_max = 2147483647
        int_min = -2147483648
        if x<0:
            pre = -1
            x = -x
        else:
            pre = 1
        ans = 0
        while x>0:
            ans = ans*10 + (x%10)
            x /= 10
        ans = pre*ans
        if ans>int_max:
            return 0
        elif ans<int_min:
            return 0
        return ans

if __name__=="__main__":
    s = Solution()
    data_in = [-123, 123, 0, 1, -1,123456,1534236469]
    for d in data_in:
        print s.reverse(d)
