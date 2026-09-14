class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        coord = sorted([(p,s) for p,s in zip(position, speed)], reverse=True)
        stack = []

        for i in coord:
            time = (target-i[0]) / i[1]
            stack.append(time)

            while len(stack) >=2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)