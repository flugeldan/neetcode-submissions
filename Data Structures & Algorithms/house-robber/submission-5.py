class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        ans = 0
        def dfs(i):
            nonlocal memo
            nonlocal ans
            localMaxMemo = nums[i]
            ans = max(ans, localMaxMemo)
            if i in memo:
                return memo[i]
            if i + 1 == len(nums) - 1 or i == len(nums) - 1:
                return localMaxMemo
            for j in range(i + 2, len(nums)):
                memo[j] = dfs(j)
                localMaxMemo = max(localMaxMemo, memo[j] + nums[i])
            ans = max(ans, localMaxMemo)
            return localMaxMemo 
        ans = 0
        dfs(0)
        dfs(1)
            
        return ans






    






        