class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if (len(s) % 2) == 1:
            return False

        for bracket in s:
            if bracket in [")", "]", "}"]:
                if not stack:
                    return False
                print(stack)
                top = stack.pop()
                if bracket == ")" and top != "(":
                    return False
                elif bracket == "]" and top != "[":
                    return False
                elif bracket == "}" and top != "{":
                    return False
            else:
                stack.append(bracket)
        
        if stack:
            return False
        return True
        