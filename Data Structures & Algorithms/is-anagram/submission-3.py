class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = {}
        seenT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in seenS:
                seenS[s[i]] = 1
            else:
                seenS[s[i]] += 1

            if t[i] not in seenT:
                seenT[t[i]] = 1
            else:
                seenT[t[i]] += 1
        
        if seenS != seenT:
            return False
        
        else:
            return True