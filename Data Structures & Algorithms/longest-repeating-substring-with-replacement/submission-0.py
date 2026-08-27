class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        window = {}

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if (r-l+1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            length = max(length, r-l+1)
        return length
# s = "XYYXXXXYYYXY"
# k = 3