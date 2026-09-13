class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        coord = []

        for i in range(len(position)):
            coord.append([position[i], speed[i]])
        
        coord = sorted(coord, reverse=True)
        stack = []

        for p,s in coord:
            curr = [p, s]
            time = (target - p) / s
            stack.append(time)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
                
        return len(stack)
