class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashcheck=set(nums)
        return False if len(hashcheck)==len(nums) else True
        