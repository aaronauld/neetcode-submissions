class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(char for char in s if char.isalnum()).lower()
        # return s == s[::-1]
        l = 0
        r = len(s) - 1

        while l <= r:
            print(s[l], s[r])
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True