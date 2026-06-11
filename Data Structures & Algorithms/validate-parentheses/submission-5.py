class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={')':'(','}':'{',']':'['}
        
        for j in s:
            if j in check:
                if stack and stack[-1] == check[j]:
                    stack.pop()
                else:
                    return False
            if j =='(' or j=='[' or j=='{':
                stack.append(j)
        return True if not stack else False
        
                

        