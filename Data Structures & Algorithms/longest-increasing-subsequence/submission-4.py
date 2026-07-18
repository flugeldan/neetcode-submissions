class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        #validate given streak
        #start new streak
        #start new streak from next element
        #continue streak without current element
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            cur = nums[i]
            take = 1 + dfs(i + 1, cur) if cur > prev else float('-inf')
            step = dfs(i + 1, prev)

            memo[(i, prev)] = max(take, step)
            return memo[(i, prev)]
        
        

        return dfs(0, float('-inf'))