class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        left=0
        right=len(height)-1
        while left<right:
            widthArea=right-left
            heightArea=min(height[left],height[right])
            area=heightArea*widthArea
            if area>maxarea:
                maxarea=area
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxarea      