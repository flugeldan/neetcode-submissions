from collections import deque
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        been = []
        stack = deque()
        for i in range(len(heights) -1, -1, -1):
            cur = heights[i]
            while stack and heights[stack[0]] < cur:
                ans[i] += 1
                stack.popleft()
            
            if stack:
                ans[i] += 1 
                stack.appendleft(i)
            else:
                stack.append(i)
        return ans
        
            

       


        