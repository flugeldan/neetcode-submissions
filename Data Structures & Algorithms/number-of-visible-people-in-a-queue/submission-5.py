from collections import deque
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = deque()
        ans = [0] * len(heights)
        for i in range(len(heights) -1, -1, -1):
            while stack and heights[stack[0]] < heights[i]:
                ans[i] += 1 
                stack.popleft()
            if stack:
                ans[i] += 1 
            stack.appendleft(i)
        return ans
        