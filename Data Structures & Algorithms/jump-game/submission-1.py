class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Rule: we just want to know at this node can I reach it? If I can we add the number of jumps it
        # offers. If this is greater than the current reachable max we increase max.

        jumps = 0
        for index, value in enumerate(nums):
            if jumps < index:
                return False

            jumps = max(index + value, jumps)
            
        return True