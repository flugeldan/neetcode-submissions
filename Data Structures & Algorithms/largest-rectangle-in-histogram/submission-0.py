class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height_index = stack.pop()
                h = heights[height_index]
                width = i if not stack else i - stack[-1] - 1
                area = width * h
                max_area = max(max_area,area)
            stack.append(i)
        return max_area

                

                

        
