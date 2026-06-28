class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        minLength = float('inf')
        for i in range(len(nums)):
            num = nums[i]
            if num >= target:
                return 1 
            
            curSum += num
            while l < i and curSum >= target:
                minLength = min(minLength, i - l + 1)
                curSum -= nums[l]
                l += 1
            
        return minLength if minLength != float('inf') else 0



        