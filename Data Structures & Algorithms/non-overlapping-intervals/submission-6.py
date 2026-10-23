class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        overlaps = 0

        curr = intervals[0]
        for interval in intervals[1:]:
            if curr[1] > interval[0]:
                overlaps += 1
            else:
                curr = interval

        return overlaps