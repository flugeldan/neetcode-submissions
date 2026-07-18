class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        ans = 0

        #validate given streak
        #start new streak
        #start new streak from next element
        #continue streak without current element
        def dfs(i, prev):
            nonlocal ans
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]


            cur = nums[i]
            take = 1 + dfs(i + 1, cur) if cur > prev else float('-inf')
            step = dfs(i + 1, prev)
            new_start = dfs(i + 1, cur)
            ans = max(take, new_start, step)
            memo[(i, prev)] = max(take, step)
            memo[(i, cur)] = new_start
            return memo[(i, prev)]
        

        return max(dfs(0, float('-inf')), ans)