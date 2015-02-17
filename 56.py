# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals)<=1:
            return intervals
        intervals.sort(key=lambda x:x.start)
        inter = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i].start>inter.end:
                ans.append(inter)
                inter = intervals[i]
            else:
                inter.end = max(inter.end, intervals[i].end)
        ans.append(inter)
        return ans

class Solution2:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x:x.start)
        ans = []
        for inter in intervals:
            if ans and inter.start<=ans[-1].end:
                ans[-1].end = max(inter.end, ans[-1].end)
            else:
                ans.append(inter)                
        return ans


s = Solution()
s2 = Solution2()
data = [
        [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)], 
        [Interval(2,4), Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)], 
        [Interval(1,4),Interval(2,3)], 
    ]
# for d in data:
#     d = s.merge(d)
#     print [(x.start, x.end) for x in d]

import time
times = 10

start = time.clock()
for i in range(times):
    for d in data:
        d = s.merge(d)
        # print [(x.start, x.end) for x in d]
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        d = s2.merge(d)
        # print [(x.start, x.end) for x in d]
print time.clock()-start