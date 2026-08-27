class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            sortedS = "".join(sorted(string))
            if sortedS not in seen:
                seen[sortedS] = []
            seen[sortedS].append(string)
        return list(seen.values())