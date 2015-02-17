class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        ans = ''
        n = len(num1)
        m = len(num2)
        for i in range(1, m+1):
            r = 0
            idx = i-1
            temp = ans[0:idx]
            l_ans = len(ans)
            for j in range(1, n+1):
                r += int(num2[-i])*int(num1[-j])
                if idx<l_ans:
                    r += int(ans[idx])
                temp += str(r%10)
                r /= 10
                idx += 1
            while r>0:
                if idx<l_ans:
                    r += int(ans[idx])
                temp += str(r%10)
                r /= 10
                idx += 1
            ans = temp
        j = 0
        for i in range(1, len(ans)):
            if ans[-i]!='0':
                break
            j = i
        return ans[0:len(ans)-j][::-1]

class Solution2:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        ans = []
        n = len(num1)
        m = len(num2)
        for i in range(1, m+1):
            r = 0
            idx = i-1
            l_ans = len(ans)
            for j in range(1, n+1):
                r += int(num2[-i])*int(num1[-j])
                if idx<l_ans:
                    r += ans[idx]
                    ans[idx] = r%10
                else:
                    ans.append(r%10)
                r /= 10
                idx += 1
            if r>0:
                ans.append(r)
        for i in range(1, len(ans)+1):
            if ans[-i]!=0:
                break
        res = ''
        for j in range(i, len(ans)+1):
            res += str(ans[-j])
        return res
        
class Solution2:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        ans = []
        n = len(num1)
        m = len(num2)
        for i in range(1, m+1):
            r = 0
            idx = i-1
            l_ans = len(ans)
            for j in range(1, n+1):
                r += int(num2[-i])*int(num1[-j])
                if idx<l_ans:
                    r += ans[idx]
                    ans[idx] = r%10
                else:
                    ans.append(r%10)
                r /= 10
                idx += 1
            if r>0:
                ans.append(r)
        for i in range(1, len(ans)+1):
            if ans[-i]!=0:
                break
        res = ''
        for j in range(i, len(ans)+1):
            res += str(ans[-j])
        return res

class Solution3:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))

import time
times = 10

s = Solution3()
s2 = Solution2()
data = [
        ['1','2'],['9','1'],['999','1'],
        ['5','6'],
        ['1','1'],['123','321'],['1','11'],['1234567890','1234567890'],['999','0']
        ]

start = time.clock()
for i in range(times):
    for d in data:
        s.multiply(d[0], d[1])
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        s2.multiply(d[0], d[1])
print time.clock()-start