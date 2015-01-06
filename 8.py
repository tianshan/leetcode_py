
class Solution:
    # @return an integer
    def atoi(self, str):
        pre = 1
        ans = 0
        up = 0
        int_max = 2147483647
        int_min = -2147483648
        flag = True
        sign = False
        e_permit = False
        for i in range(0, len(str)):
            if flag and str[i]==' ':
                continue
            flag=False

            if sign==False and str[i]=='-':
                pre = -1
                sign=True
                continue
            if sign==False and str[i]=='+':
                sign=True
                continue

            # if e_permit and (str[i]=='e' or str[i]=='E'):
            #     for j in range(i+1, len(str)):
            #         if str[j]=='+' and j==i+1:
            #             continue
            #         if str[j]<'0' or str[j]>'9':
            #             break
            #         up = up*10+int(str[j])
            #     break

            if str[i]<'0' or str[i]>'9':
                break

            ans = ans*10+int(str[i])
            if pre*ans>int_max:
                return int_max
            if pre*ans<int_min:
                return int_min
            e_permit = True

        if up>9:
            ans = int_max
        else:
            for i in range(up):
                ans = ans * 10
        ans = pre*ans

        if ans>int_max:
            return int_max
        if ans<int_min:
            return int_min        
        return ans

if __name__=="__main__":
    data_in = ['1234567890123401231412412312','-1', '1e3','-12E10','+1', '  010', '-11e530408314', 'e2', '  ', '  123  A', '1e ', '-0012a42', '-2147483648', '   -115579378e25']
    s = Solution()
    for d in data_in:
        print '%r %r' %(d,s.atoi(d))
