class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        node = intervals[0]
        overlaps = 0
        
        for interval in intervals[1:]:
            if node[1] > interval[0]:
                overlaps += 1
            else:
                node = interval

        return overlaps