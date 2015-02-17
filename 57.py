# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals)==0:
            return [newInterval]
        if newInterval==None:
            return intervals
        if newInterval.start<intervals[0].start:
            intervals[0],newInterval = newInterval, intervals[0]
        ans = []
        for inter in intervals:
            if ans and inter.start<=ans[-1].end:
                ans[-1].end = max(inter.end, ans[-1].end)
            else:
                ans.append(inter)

            if newInterval and ans[-1].end>=newInterval.start:
                if ans[-1].start>newInterval.end:
                    ans[-1], newInterval = newInterval, ans[-1]
                    ans.append(newInterval)
                else:
                    ans[-1].start = min(ans[-1].start, newInterval.start)
                    ans[-1].end = max(ans[-1].end, newInterval.end)
                newInterval = None
        if newInterval:
            ans.append(newInterval)
        return ans



class Solution2:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        ans = []
        for inter in intervals:
            if ans and inter.start<=ans[-1].end:
                ans[-1].end = max(inter.end, ans[-1].end)
            else:
                ans.append(inter)                
        return ans

class Solution3:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        while i < len(intervals):
            if newInterval.start <= intervals[i].end:
                if newInterval.end < intervals[i].start:
                    break
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(newInterval)
        result += intervals[i:]
        return result

class Solution4:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        i = 0
        while i<len(intervals):
            if newInterval.start <= intervals[i].end:
                if newInterval.end < intervals[i].start:
                    break
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                del intervals[i]
            else:
                i += 1
        intervals[i:i] = [newInterval]
        return intervals

s = Solution4()
s2 = Solution3()
data = [
        ([Interval(1,3),Interval(6,9)], Interval(2,5)),
        ([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)], Interval(4,9)),
        ([Interval(1,2), Interval(3,6),Interval(8,10),Interval(15,18)], Interval(4,9)),
        ([Interval(1,2),Interval(3,3)], Interval(4,9)),
        ([Interval(1,3),Interval(6,9)], Interval(-1,0)),
        ([Interval(1,3),Interval(6,9)], Interval(10,11)),
        ([Interval(1,5)], Interval(0,3)),
        ([Interval(0,5),Interval(9,12)], Interval(7,16)),
    ]
# for d in data:
#     d = s.insert(d[0], d[1])
#     print [(x.start, x.end) for x in d]

import time
times = 100

start = time.clock()
for i in range(times):
    for d in data:
        d = s.insert(d[0], d[1])
        # print [(x.start, x.end) for x in d]
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        d = s2.insert(d[0], d[1])
        # print [(x.start, x.end) for x in d]
print time.clock()-start