class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        countS, countT = {}, {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        l = 0
        ans, length = [-1,-1], float("INF")
        have, need = 0, len(countT)

        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < length:
                    length = r-l+1
                    ans=[l, r]

                if s[l] in countT:
                    countS[s[l]] -= 1   
                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1

        l, r = ans
        if length == float("INF"):
            return ""

        return s[l:r+1]