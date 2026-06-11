class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        been = set()
        l = 0
        n = len(s)
        maxWindow = float('-inf')
        for i in range(n):
            if been and s[i] in been:
                while s[i] in been:
                    been.discard(s[l])
                    l += 1 
            been.add(s[i])
            maxWindow = max(maxWindow, i - l + 1)
        return maxWindow


        