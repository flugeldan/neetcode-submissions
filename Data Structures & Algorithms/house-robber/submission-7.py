class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        memo = {}
        ans = 0
        def dfs(i):
            nonlocal memo
            nonlocal ans
            localMaxMemo = nums[i]
            for j in range(i + 2, len(nums)):
                if j not in memo:
                    memo[j] = dfs(j)
                localMaxMemo = max(localMaxMemo, memo[j] + nums[i])
            ans = max(ans, localMaxMemo)
            return localMaxMemo 
        ans = 0
        dfs(0)
        dfs(1)
            
        return ans






    






        