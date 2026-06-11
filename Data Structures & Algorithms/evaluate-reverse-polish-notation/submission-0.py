
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashcheck={'+','-','*','/'}
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in hashcheck:
                if tokens[i]=='+':
                    if len(stack)>=2:
                        a=stack.pop()
                        b=stack.pop()
                        stack.append(a+b)
                elif tokens[i]=='-':
                    if len(stack)>=2:
                        a=stack.pop()
                        b=stack.pop()
                        stack.append(b-a)
                elif tokens[i]=='*':
                    if len(stack)>=2:
                        a=stack.pop()
                        b=stack.pop()
                        stack.append(b*a)
                elif tokens[i]=='/':
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
                        

                    



        