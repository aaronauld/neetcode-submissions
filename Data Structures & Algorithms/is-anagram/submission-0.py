class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS = {}
        seenT = {}
        for i in range(len(s)):
            if s[i] in seenS:
                seenS[s[i]] += 1
            else:
                seenS[s[i]] = 1

            if t[i] in seenT:
                seenT[t[i]] += 1
            else:
                seenT[t[i]] = 1
            # seenS[s[i]] = 1 + seenS.get(s[i], 0)
            # seenT[t[i]] = 1 + seenT.get(t[i], 0)
        return seenS == seenT