class TimeMap:

    def __init__(self):
        self.structure = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.structure:
            self.structure[key] = []
        self.structure[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.structure.get(key, [])

        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
