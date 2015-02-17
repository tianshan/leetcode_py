class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num)<3:
            return 0
        num.sort()
        maxt = num[-1]+num[-2]+num[-3]
        if target>=maxt:
            return maxt
        mint = num[0]+num[1]+num[2]
        if target<=mint:
            return mint
        if (maxt-target)<(target-mint):
            minans = maxt-target
        else:
            minans = mint-target
        for i in range(len(num)-2):
            if minans==0:
                break
            l = i+1
            r = len(num)-1
            while l<r:
                temp = num[i]+num[l]+num[r]
                if abs(temp-target)<abs(minans):
                    minans = temp-target
                if minans==0:
                    break
                if temp>target:
                    r -= 1
                elif temp<target:
                    l += 1
        return target+minans

if __name__=='__main__':
    s = Solution()
    data = [([-1,2,1,-4], 1)]
    for d in data:
        print d,s.threeSumClosest(d[0],d[1])
