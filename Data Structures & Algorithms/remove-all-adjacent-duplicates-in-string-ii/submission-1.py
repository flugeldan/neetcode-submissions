class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        prev, streak = None, 0
        for i, char in enumerate(s):
            stack.append(char)
            n = len(stack)
            if n >= k and stack[n - k] == stack[-1]:
                if all(stack[i] == stack[-1] for i in range(n - k, n)):
                    for _ in range(k):
                        stack.pop()
        return ''.join(stack)




            
            
            
                    
                    
            
        

                    



        