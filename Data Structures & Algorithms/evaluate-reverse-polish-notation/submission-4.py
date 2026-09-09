class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                val2 = stack.pop()
                val1 = stack.pop()
                # print(val1, val2, int(val1 / val2))
                stack.append(int(val1 / val2))
            else:
                stack.append(int(char))
        
        return stack[0]