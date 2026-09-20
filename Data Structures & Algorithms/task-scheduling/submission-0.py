class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Restate: minimum cpu cycles to complete tasks where the gap between identical tasks is at least n
        # Scarce/Demand: number of time slots / number of tasks
        # Rule:  Max heap from the count of time slots. We then use a queue to keep track 
        # of the cooldown time until that task can be added back to the heap. If there is nothing in the heap
        # and there are items in the queue, it will be an idle value
        # Reason: we want to process the item will the most occurences first as that has the most future 
        # cooldowns. Running early starts the cooldown quicker. Running a lower count delays that cooldown.

        taskCounts = defaultdict(int)
        for task in tasks:
            taskCounts[task] += 1
        maxHeap = list(taskCounts.values())
        heapq.heapify_max(maxHeap)

        iterations = 0
        queue = deque()

        while maxHeap or queue:
            iterations += 1
            
            if not maxHeap:
                iterations = queue[0][1]
            
            else:
                curr = heapq.heappop_max(maxHeap)
                if curr != 1:
                    queue.append([curr-1, iterations + n])

            if queue and queue[0][1] == iterations:
                heapq.heappush_max(maxHeap, queue.popleft()[0])

        return iterations
