class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            elif i == len(nums) - 1 or i == len(nums) - 2:
                return nums[i]
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i + 2), dfs(i + 3)) + nums[i]

            return memo[i]

            
        return max(dfs(0), dfs(1))






    






        