class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        elif len(nums) == 1:
            return True
        i, n = 0, len(nums)
        while i < n:
            if i == n - 1 or i + nums[i] >= n - 1:
                return True
            elif i < n - 1 and nums[i] == 0:
                return False
            j = i + 1
            pos = nums[i]
            maxVal, maxValPos = nums[j], nums[j + 1]


            while nums[i] > 0:
                if nums[j] >= maxVal:
                    maxVal = nums[j]
                    maxValPos = j
                if nums[j] > 0:
                    if j + nums[j] > maxVal + maxValPos:
                        pos = j
                    else:
                        pos = maxValPos
                nums[i] -= 1 
            
                j += 1 
            i = pos
   
        return True




            
            
            

            
            
        return True
                

            
            


        
        