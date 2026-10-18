class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringDict = defaultdict(list)

        for string in strs:
            chars = tuple(sorted(string))
            stringDict[chars].append(string)

        return list(stringDict.values())