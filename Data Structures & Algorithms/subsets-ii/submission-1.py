class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        def dfs(i,arr):
            ans.append(arr)
            for j in range(i + 1, len(nums)):
                if nums[j] != nums[j - 1] or j == i + 1:
                    dfs(j, arr + [nums[j]])

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                dfs(i, [nums[i]])
    

        return ans








