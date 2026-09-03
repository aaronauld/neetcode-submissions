class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        for i in range(len(nums)):
            seen[nums[i]] = 1 + seen[nums[i]]

        return sorted(seen, key=seen.get, reverse=True)[:k]
