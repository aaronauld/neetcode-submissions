class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            
            while stack and val > stack[-1][0]:
                top = stack.pop()
                result[top[1]] = i - top[1]
            stack.append([val, i])

        return result