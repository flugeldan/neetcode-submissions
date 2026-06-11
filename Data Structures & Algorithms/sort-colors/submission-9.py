from collections import deque
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a = deque([0,0,0])
        n = len(nums)
        for i in range(len(nums)):
            a[nums[i]] += 1 
        for i in range(n):
            if a[0] > 0:
                nums[i] = 0 
                a[0] -= 1 
            elif a[1] > 0:
                nums[i] = 1 
                a[1] -= 1 
            else:
                nums[i] = 2 
                a[2] -= 1 
                
