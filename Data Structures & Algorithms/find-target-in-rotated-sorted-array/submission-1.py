class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ans = -1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] <= nums[r]:
                r = m
        pivot = l
        
        if nums[pivot] <= target <= nums[len(nums)-1]:
            left = pivot
            right = len(nums)-1
        else:
            left = 0
            right = pivot - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1