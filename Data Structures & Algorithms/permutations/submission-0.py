class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i, cur, been):
            been.add(i)
            cur.append(nums[i])
            if len(cur) >= len(nums):
                ans.append(cur.copy())
                been.discard(i)
                cur.pop()
                return
            for j in range(len(nums)):
                if j not in been:
                    dfs(j, cur, been)
            
            been.discard(i)
            cur.pop()

        for i in range(len(nums)):
            dfs(i, [], set())
        return ans
