class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashcheck={}
        for i in range(len(nums)):
            if target-nums[i] in hashcheck:
                return [hashcheck[target-nums[i]], i]
            hashcheck[nums[i]]=i
        
        