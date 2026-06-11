class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        count=set()
        l=0
        for i in range(len(s)):
            while s[i] in count and count:
                count.discard(s[l])
                l+=1
            count.add(s[i])
            max_length=max(max_length, len(count))


        return max_length



        
        