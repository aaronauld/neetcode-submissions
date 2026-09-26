class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Rule: if the sum ever becomes negative then we can ignore all the indexes up to that point
        # because we are going to have to sacrifice other values to make that positive.
        total = 0
        sub = nums[0]

        for num in nums:  
            if total < 0:
                total = 0
            total += num
            sub = max(sub, total)
        
        return sub