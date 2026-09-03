class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringDict = {}

        for string in strs:
            characters = "".join(sorted(string))
            if characters not in stringDict:
                stringDict[characters] = []
            stringDict[characters].append(string)
        
        return list(stringDict.values())