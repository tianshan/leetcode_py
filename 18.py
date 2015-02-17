class Solution:
    # O(n^3)
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num)<4:
            return []
        num.sort()
        ans = []
        for i in range(len(num)-3):
            if i>0 and num[i-1]==num[i]:
                continue
            re = self.threeSum(num, i+1, target-num[i])
            if len(re)!=0:
                for r in re:
                    ans.append([num[i]]+r)
        return ans

    def threeSum(self, num, start, target):
        n_len = len(num)
        if n_len-start<3:
            return []
        ans = []
        for i in range(start, n_len):
            if i>start and num[i-1]==num[i]:
                continue
            l = i+1
            r = n_len-1
            # print num[i],num[l],num[r]
            while l<r:
                if num[l]+num[r]+num[i]<target:
                    l += 1
                elif num[l]+num[r]+num[i]==target:
                    ans.append([num[i], num[l], num[r]])
                    l += 1
                    while l<r and num[l]==num[l-1]:
                        l += 1
                    r -= 1
                    while l<r and num[r]==num[r+1]:
                        r -= 1
                else:
                    r -= 1
        return ans

class Solution2:
    # O(n^2*logn) 358ms
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        sum2 = dict()
        num.sort()
        for i in range(1, len(num)):
            # if i>1 and num[i-1]==num[i]:
            #     continue
            for j in range(i+1, len(num)):
                # if j>i+1 and num[j-1]==num[j]:
                #     continue
                key = num[i]+num[j]
                if sum2.has_key(key)==False:
                    sum2[key] = list()
                sum2[key].append((i, (num[i],num[j]) ))
        ans = []
        for i in range(len(num)-3):
            if i>0 and num[i-1]==num[i]:
                continue
            for j in range(i+1, len(num)-2):
                if j>i+1 and num[j-1]==num[j]:
                    continue
                key = num[i]+num[j]
                for a in sum2.get(target-key, []):
                    if a[0]<=j:
                        continue
                    ans.append((num[i],num[j])+a[1])
        ans = list(set(ans))
        ans = [list(x) for x in ans]
        return ans

class Solution3:
    # O(n^2*logn) 426ms
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num)<4:
            return []
        sum2 = dict()
        num.sort()
        for i in range(2, len(num)):
            for j in range(i+1, len(num)):
                key = num[i]+num[j]
                if sum2.has_key(key)==False:
                    sum2[key] = dict()
                sum2[key][num[i]] = i
        ans = []
        for i in range(len(num)-3):
            if i>0 and num[i-1]==num[i]:
                continue
            for j in range(i+1, len(num)-2):
                if j>i+1 and num[j-1]==num[j]:
                    continue
                key = target-num[i]-num[j]
                for k,v in sum2.get(key, dict()).items():
                    if v<=j:
                        continue
                    ans.append([num[i],num[j],k,key-k])
        return ans

if __name__=='__main__':
    s = Solution3()
    data = [([1,0,-1,0,-2,2],0), ([-1,-1,-1,-1,0,0,0,0,1,1,1,1], 0)]
    for d in data:
        print s.fourSum(d[0],d[1])