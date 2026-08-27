class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        time = 0

        while l <= r:
            k = (l + r) // 2
            tmpTotal = 0
            for pile in range(len(piles)):
                tmpTotal += math.ceil(piles[pile]/k)
            if tmpTotal <= h:
                time = k
                r = k - 1
            elif tmpTotal > h:
                l = k + 1
        return time