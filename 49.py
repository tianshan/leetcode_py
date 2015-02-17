class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        n = len(strs)
        if n==0:
            return []
        hv = []
        for s in strs:
            s = sorted(s)
            r = 0
            for c in s:
                if c==' ':
                    continue
                r = r*30+ord(c)
            hv.append(r)
        idx = [i for i in range(n)]
        idx = sorted(idx, key=lambda x:hv[x])
        last = None
        ans = []
        i = 0
        while i<n:
            if last!=None and hv[idx[i]]==last:
                i = i-1
                while i<n and hv[idx[i]]==last:
                    ans.append(strs[idx[i]])
                    i += 1
            else:
                last = hv[idx[i]]
                i += 1
        return ans

class Solution2:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        hv = dict()
        for i,s in enumerate(strs):
            key = tuple(sorted(s))
            if hv.has_key(key)==False:
                hv[key] = list()
            hv[key].append(i)
        ans = []
        for k,v in hv.items():
            if len(v)>1:
                ans += [strs[i] for i in v]
        return ans

import time
times = 100

s = Solution()
s2 = Solution2()
data = [['tea', 'eat', 'qwe','etaa', 'eta'],["tea","and","ate","eat","dan"],[]]

start = time.clock()
for i in range(times):
    for d in data:
        s.anagrams(d)
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        s2.anagrams(d)
print time.clock()-start
