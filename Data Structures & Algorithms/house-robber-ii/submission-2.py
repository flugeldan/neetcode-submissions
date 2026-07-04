class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            nums = nums[::-1]
        memo = {}
        def rob(i, bound):
            if i >= bound:
                return 0 
            if i == len(nums) - 1 or i == len(nums) - 2:
                return nums[i]
            if i in memo:
                return memo[i]
            
            memo[i] = nums[i] + max(rob(i + 2, bound), rob(i + 3, bound))

            return memo[i]
        firstrob = rob(0, len(nums) - 1)
        memo = {}
        secondrob = rob(1, len(nums))
        return max(firstrob, secondrob)
            



  


        