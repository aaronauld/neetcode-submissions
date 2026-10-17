class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            rem = target - val

            if val in seen:
                return [seen[val], i]
            
            seen[rem] = i