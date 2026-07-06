class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        hash_ = set(nums)
        cur = max_ = 1
        for num in nums:
            j = num
            while j - 1 in hash_:
                cur += 1 
                hash_.discard(j)
                j -= 1 
            j = num
            while j + 1 in hash_:
                cur += 1 
                hash_.discard(j)
                j += 1 
            max_ = max(cur, max_)
            cur = 1 


        return max_
