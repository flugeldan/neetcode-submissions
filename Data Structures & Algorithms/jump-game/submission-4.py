class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        elif len(nums) == 1:
            return True
        n = len(nums)
        lastNonNull = nums[0]
        canMaxJump = 0 + nums[0]
        for i in range(len(nums) - 1):
            if i > canMaxJump:
                return False
            
            if nums[i] > 0:
                if i + nums[i] >= canMaxJump:
                    canMaxJump = i + nums[i]
            if nums[i] + i >= n - 1:
                return True
        return False
        
            
         



            
            


        
        