class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightP = [0] * len(nums)
        leftP = [0] * len(nums)
        result = [0] * len(nums)

        leftP[0] = rightP[-1] = 1
        for i in range(1, len(nums)):
            leftP[i] = leftP[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            rightP[i] = rightP[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = leftP[i] * rightP[i]

        return result 
        
