class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        lmax, rmax = height[l], height[r]
        total = 0
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(height[l], lmax)
                total += lmax - height[l]
            else: 
                r -= 1
                rmax = max(height[r], rmax)
                total += rmax - height[r]
        return total