class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            length = max(length, r-l+1)
        return length

        # chars = {}
        # l = 0
        # length = 0

        # for r in range(len(s)):
        #     chars[s[r]] = 1 + chars.get(s[r], 0)
        #     while chars[s[r]] > 1:
        #         chars[s[l]] -= 1
        #         l += 1
        #     length = max(length, r-l+1)
        # return length