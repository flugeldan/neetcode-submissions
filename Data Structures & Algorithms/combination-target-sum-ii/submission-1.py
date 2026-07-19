class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        been = set()
        ans = []
        def dfs(i, arr, cur_sum):
            if cur_sum == target:
                ans.append(arr)
                return
            if i >= len(candidates) or cur_sum > target:
                return
            dfs(i + 1, arr + [candidates[i]], cur_sum + candidates[i])
            j = i + 1 
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, arr, cur_sum)
            

        dfs(0, [], 0)
        return ans






  

        