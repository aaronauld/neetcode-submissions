class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Minimize the number of cycle to complete all the tasks
        # same tasks must be separated by n
        # any order
        # Rule: the values that occur the most, must be started ASAP. Because they'll require the longest
        # total cooldown time. Use a max heap to track how many more occurences there are. Also need to track
        # when a tasks can be started again. So we should have a queue that tells us when a task is ready

        groupedTasks = {}
        for task in tasks:
            groupedTasks[task] = 1 + groupedTasks.get(task, 0)
        
        groupedTasks = list(groupedTasks.values())
        groupedTasks.sort(reverse=True)
        heapq.heapify_max(groupedTasks)

        iterations = 0
        queue = deque()

        while groupedTasks or queue:
            iterations += 1
            
            if not groupedTasks:
                iterations = queue[0][1]
            
            else:
                curr = heapq.heappop_max(groupedTasks)
                if curr != 1:
                    queue.append([curr-1, iterations + n])

            if queue and queue[0][1] == iterations:
                heapq.heappush_max(groupedTasks, queue.popleft()[0])

        return iterations
