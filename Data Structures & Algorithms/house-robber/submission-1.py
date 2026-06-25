class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAmount = 0
        memo = {}


        def dfs(i):
            nonlocal maxAmount
            nonlocal memo
            if i >= len(nums):
                return 0
            if i + 1 == len(nums) - 1 or i == len(nums) - 1:
                return nums[i]
            if i in memo:
                return memo[i]
            localMaxMemo = nums[i]
            for j in range(i + 2, len(nums)):
                memo[j] = dfs(j)
                localMaxMemo = max(localMaxMemo, memo[j] + nums[i])
                


            return localMaxMemo 
        ans = 0
        for i in range(len(nums)):
            memo[i] = dfs(i)
            ans = max(ans, memo[i])
            
        return ans






    






        