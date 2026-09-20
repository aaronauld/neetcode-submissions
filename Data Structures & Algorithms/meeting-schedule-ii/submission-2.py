"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
# Restate: We are interested in finding the minimum number of rooms where meetings dont overlap.
# Scarce/Demand: the scarce item is room time, whether a room is free / demand is the number of meetings
# Rule: Sort by start time and we need to track the end times of all currently running meetings so that when the first one is free we add it as long as the start is at / after the end
# Anti: [1,3],[1,4],[4,40],[5,10],[15,20] answer is 2 rooms. If you were to take 1,3 or 1,4 they will always be separate rooms. any number that comes next that won't form a new room will always satisfy both intervals assuming
        intervals.sort(key= lambda x:x.start)
        rooms = []

        for meeting in intervals:
            if rooms and meeting.start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, meeting.end)
        
        return len(rooms)
            