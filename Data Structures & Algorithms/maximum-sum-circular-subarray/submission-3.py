class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        minSum = curMinSum = nums[0]
        n = sum(nums)
        l, w1, w2 = 0, 0, 0
        for i in range(1, len(nums)):
            num = nums[i]
            curSum = max(curSum + num, num)
            maxSum = max(maxSum, curSum)

            curMinSum = min(curMinSum + num, num)
            minSum = min(curMinSum, minSum)
        
        if n - minSum == 0:
            return maxSum

        return max(maxSum, n - minSum)


        
        



        
   

