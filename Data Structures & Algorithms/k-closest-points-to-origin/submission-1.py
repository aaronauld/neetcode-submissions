class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush_max(maxHeap, [distance, point])
        
            while len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        return [x[1] for x in maxHeap]