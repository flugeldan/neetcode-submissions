class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        

        def dfs(i, cur, total):
            nonlocal res
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return 
            for j in range(i, len(nums)):
                dfs(j, cur + [nums[j]], total + nums[j])
        dfs(0, [], 0)
        return res
             

                 

        