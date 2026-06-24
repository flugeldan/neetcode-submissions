from collections import deque
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        been = []
        stack = []
        for i in range(len(heights)):
            cur = heights[i]
            while stack and cur >= heights[stack[-1]]:
                index = stack.pop()
                ans[index] += i - index
            for j in range(len(stack) - 1):
                ans[stack[j]] -= 1 
            stack.append(i)
            
        n = len(stack)
        
        
        while stack:            
            x = stack.pop()
            ans[x] += len(ans) - 1 - x

        return ans
       


        