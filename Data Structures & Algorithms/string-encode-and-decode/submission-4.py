class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ""

        for string in strs:
            combined += f"{len(string)}#{string}"
        
        print(combined)
        return combined

    def decode(self, s: str) -> List[str]:
        i = 0
        words = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            words.append(s[j+1 : j+1+length])
            i = j + 1 + length

        return words