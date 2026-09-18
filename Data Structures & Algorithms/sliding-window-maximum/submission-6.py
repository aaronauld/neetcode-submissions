class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        queue = deque()
        ans = []

        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if (r-l+1) >= k:
                ans.append(nums[queue[0]])
                l += 1
        
        return ans