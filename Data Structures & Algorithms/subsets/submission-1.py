class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]

        for num in nums:
            ans.append([num])
            n = len(ans)
            arrays = [ans[x] + [num] for x in range(1,n) if num not in ans[x]]
            ans.extend(arrays)
        return ans


        
        