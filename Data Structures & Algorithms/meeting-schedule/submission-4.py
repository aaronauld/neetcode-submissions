"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.end)
        if len(intervals) == 0:
            return True

        prev = intervals[0]

        for interval in intervals[1:]:
            if prev.end > interval.start:
                return False
        
            prev = interval
        return True