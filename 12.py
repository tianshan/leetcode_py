class Solution:
    # @return a string
    def intToRoman(self, num):
        nums = [1000,500,100,50,10,5,1]
        cs = ['M','D','C','L','X','V','I']
        ans = ''
        for i in range(len(nums)):
            if num>=nums[i]:
                x = num/nums[i]
                if x==4:
                    ans += cs[i]+cs[i-1]
                    num -= x*nums[i]
                elif i&1==1 and (nums[i]+nums[i]-nums[i+1])<=num:
                    ans += cs[i+1]+cs[i-1]
                    num -= nums[i]+nums[i]-nums[i+1]
                else:
                    ans += cs[i]*x
                    num -= x*nums[i]
        return ans

if __name__=='__main__':
    s = Solution()
    # for d in [1,4,9,11,15,50,40]:
    #     print d,s.intToRoman(d)
    while 1:
        d = raw_input()
        print s.intToRoman(int(d))