class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0

        while l <= r:
            m = (l+r) // 2
            totalSum = 0
            
            for pile in piles:
                totalSum += math.ceil(pile/m)

            if totalSum <= h:
                ans = m
                r = m - 1
            
            elif totalSum > h:
                l = m + 1
        
        return ans
