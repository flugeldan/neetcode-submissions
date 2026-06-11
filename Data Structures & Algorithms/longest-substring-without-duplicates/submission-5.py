from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l, j = 0,  0
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                longest = max(longest, j - l + 1)
                j += 1
            else:
                seen.discard(s[l])
                l += 1
        return longest








        