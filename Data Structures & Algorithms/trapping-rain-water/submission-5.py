class Solution:
    def trap(self, height: List[int]) -> int:
        waterAmount=0
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        while left<right:
            if rightmax>leftmax:
                left+=1
                leftmax=max(leftmax, height[left])
                waterAmount+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax, height[right])
                waterAmount+=rightmax-height[right]
                
        return waterAmount

        