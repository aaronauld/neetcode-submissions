class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Problem: we want to remove the minimum number of intervals to have a non overlapping sequence
        # Scarce/Demand: timeline is what is limited / intervals that need a spot
        # Rule: sort by end time taking the interval that consumes the least on the timeline
        intervals = sorted(intervals, key=lambda x:x[1])
        prev = intervals[0]
        removed = 0

        for interval in intervals[1:]:
            if prev[1] > interval[0]:
                removed += 1
            else:
                prev = interval
        
        return removed