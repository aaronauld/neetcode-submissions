class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left = 0
        # right = len(numbers)-1
        # total = 0
        # while left < right:
        #     total = numbers[left] + numbers[right]
        #     if total == target:
        #         return [left+1, right+1]
        #     elif total < target:
        #         left += 1
        #     else:
        #         right -= 1
        seen = {}
        for i,num in enumerate(numbers):
            remainder = target - num
            if remainder in seen:
                return [seen[remainder]+1, i+1]
            seen[num] = i
