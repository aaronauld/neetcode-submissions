class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            rem = target - val

            if rem in seen:
                return [seen[rem], i]
            
            seen[val] = i