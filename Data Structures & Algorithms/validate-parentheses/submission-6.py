class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        f = {')', '}', ']'}
        d = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c in d:
                if stack[-1] == d[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


        