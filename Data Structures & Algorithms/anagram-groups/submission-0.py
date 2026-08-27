class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempDict = {}
        for string in strs:
            sortedS = "".join(sorted(string))
            if sortedS not in tempDict:
                tempDict[sortedS] = []
            tempDict[sortedS].append(string)
        return list(tempDict.values())