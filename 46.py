
import time

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    # 84ms need import time
    def permute(self, num):
        ans = [tuple(i) for i in itertools.permutations(num,len(num))]
        ans = [list(i) for i in set(ans)]
        return ans

class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integers
    # slower than up
    def permute(self, num):
        num.sort()
        return self.per(num)

    def per(self, num):
        if len(num)==1:
            return [num]
        ans = []
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:
                continue
            temp = num[:]
            temp.pop(i)
            re = [[num[i]]+x for x in self.per(temp)]
            ans += re
        return ans

class Solution22:
    # @param num, a list of integer
    # @return a list of lists of integers
    # slower than up
    def permute(self, num):
        return self.per(num)

    def per(self, num):
        if len(num)==1:
            return [num]
        ans = []
        for i in range(len(num)):
            temp = num[:]
            temp.pop(i)
            re = [[num[i]]+x for x in self.per(temp)]
            ans += re
        return ans

class Solution3:
    # @param num, a list of integer
    # @return a list of lists of integers
    # slower than up
    def permute(self, num):
        num.sort()
        return self.per(num, 0)

    def per(self, num, l):
        n = len(num)
        if n==1:
            return [num]
        ans = []
        for i in range(l, n):
            if i>l and num[i]==num[i-1]:
                continue
            if i>l:
                num[l],num[i] = num[i],num[l]
            re = [[num[i]]+x for x in self.per(num, l+1)]
            if i>l:
                num[l],num[i] = num[i],num[l]
            ans += re
        return ans

class Solution32:
    # @param num, a list of integer
    # @return a list of lists of integers
    # slower than up
    def permute(self, num):
        ans = []
        self.per(num, 0, len(num), ans)
        return ans

    def per(self, num, l, n, ans):
        if l>=n:
            ans.append(num[:])
            return
        for i in range(l, n):
            if i>l:
                num[l],num[i] = num[i],num[l]
            self.per(num, l+1, n, ans)
            if i>l:
                num[l],num[i] = num[i],num[l]

class Solution4:
    # @param num, a list of integer
    # @return a list of lists of integers
    # slower than up
    def permute(self, num):
        num.sort()
        return self.perm(num)

    def perm(self, num):
        if(len(num)<=1):  
            return [num]  
        r=[]  
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:
                continue
            s=num[:i]+num[i+1:]
            p=self.perm(s)  
            for x in p:  
                r.append(num[i:i+1]+x) 
        return r
        

s = Solution()
s2 = Solution22()
s3 = Solution32()
s4 = Solution4()
times = 100
data = [[1,2,3],[1,1,2],[1]]
for d in data:
    print s3.permute(d)

start = time.clock()
for i in range(times):
    import itertools
    s.permute([1,2,3])
print time.clock()-start



start = time.clock()
for i in range(times):
    s2.permute([1,2,3])
print time.clock()-start

start = time.clock()
for i in range(times):
    s3.permute([1,2,3])
print time.clock()-start


# start = time.clock()
# for i in range(times):
#     s4.permute([1,2,3])
# print time.clock()-start