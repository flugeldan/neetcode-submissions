class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = cur = nums[0]
        

        for num in nums[1:]:
            cur = max(num, cur + num)
            maxSum = max(cur, maxSum)
        
        return maxSum
        