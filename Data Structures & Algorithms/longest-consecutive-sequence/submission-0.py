class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashcheck = set(nums)
        max_streak=0
        for num in hashcheck:
            if num-1 not in hashcheck:
                current_streak=1
                i=1
                while num+i in hashcheck:
                    current_streak+=1
                    i+=1
                max_streak=max(max_streak, current_streak)
        return max_streak


        