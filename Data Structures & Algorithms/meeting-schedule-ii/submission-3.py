"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Minmize the no. of rooms such that all meetings happen without conflicts
        # input = [[8,9], [9,11], [7,10], [13,20], [12,14]]
        # output = 2, (8-9, 9-11, 13-20), (7-10, 12-14)

        # Rule: sort on the start time, and track each interval in the order that they will finish (min heap)
        # length of the heap will represent the max number of rooms
        intervals.sort(key=lambda x:x.start)
        rooms = []

        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, interval.end)

        return len(rooms)
