class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]

        for num in nums:
            ans.append([num])

            for x in list(ans):
                if x and num not in x:
                    m = x + [num]
                    ans.append(m)
        return ans


        
        