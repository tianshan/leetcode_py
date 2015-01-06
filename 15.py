class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        sum2 = dict()
        ans = set()
        for i,n in enumerate(num):
            a = sum2.get(-n, None)
            if a!=None:
                for t in a:
                    ans.add(tuple(sorted([t[0], t[1], n])))
            for j in range(0, i):
                t_sum2 = n+num[j]
                if n<num[j]:
                    t = (n,num[j])
                else:
                    t = (num[j],n)
                if sum2.has_key(t_sum2)==False:
                    sum2[t_sum2] = set()
                sum2[t_sum2].add(t)
        ans = [list(x) for x in ans]
        return ans

if __name__=='__main__':
    s = Solution()
    data = [[-1,0,1,2,-1,-4],[-1,0,1,-1]]
    for d in data:
        print s.threeSum(d)

                
