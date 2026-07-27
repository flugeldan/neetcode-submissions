class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i, char in enumerate(s):
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0:
                    stack.pop()
        new = ''
        for char, count in stack:
            new += char * count
        return new
            
                
            

            




            
            
            
                    
                    
            
        

                    



        