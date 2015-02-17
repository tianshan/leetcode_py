class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        n_len = len(num)
        if n_len<3:
            return []
        num.sort()
        sum2 = dict()
        ans = []]
        
        n_max = num[-1]
        for i,n in enumerate(num):
            if n>=0 and (i==0 or (i>0 and num[i]!=num[i-1])):
                for t in sum2.get(-n, []):
                    ans.append(t+[n])
            if n<=0 and i>0 and n==num[i-1]:
                if i==1 or (n!=num[i-2]):
                    t_sum2 = n*2
                    if sum2.has_key(t_sum2)==False:
                        sum2[t_sum2] = list()
                    sum2[t_sum2].append([n,n])
                continue
            for j in range(0, i):
                t_sum2 = n+num[j]
                if t_sum2+num[-1]<0:
                    continue
                if t_sum2+n>0:
                    break
                if j>0 and num[j]==num[j-1]:
                    continue
                if sum2.has_key(t_sum2)==False:
                    sum2[t_sum2] = list()
                sum2[t_sum2].append([num[j],n])
        return ans

class Solution2:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        n_len = len(num)
        if n_len<3:
            return []
        ans = []
        num.sort()
        for i in range(n_len-2):
            if i>0 and num[i-1]==num[i]:
                continue
            l = i+1
            r = n_len-1
            while l<r:
                if num[l]+num[r]<-num[i]:
                    l += 1
                elif num[l]+num[r]==-num[i]:
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


if __name__=='__main__':
    
    data = [
            [-1,0,1,2,-1,-4],
            [-1,0,1,-1],
            [-2,-2,-2,-2,-1,-1,-1,-1,1,1,1,1,1,0,0,0,0,0,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4],
            [-1,0,1,2,-1,-4,-1,-1,-2,-3,-4]]
    s = Solution()
    for d in data:
        print s.threeSum(d)
    print ''
    s = Solution2()
    for d in data:
        print s.threeSum(d)

                
