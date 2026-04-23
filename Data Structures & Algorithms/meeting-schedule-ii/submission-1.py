"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        time = defaultdict(int)
        for interval in intervals:
            time[interval.start] += 1
            time[interval.end] -= 1
        maxT = max(time.keys())
        res = 0
        count = 0
        for t in range(0,maxT):
            count += time[t]
            if count > res:
                res = count
        return res



        