class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            new = abs(first - second)
            if new != 0:
                heapq.heappush(maxHeap, -new)
        
        if maxHeap:
            return -maxHeap[0] 
        
        return 0