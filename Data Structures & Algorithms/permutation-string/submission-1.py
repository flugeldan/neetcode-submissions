from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        been = Counter(s1)
        if Counter(s2[:len(s1)]) == been:
            return True
        elif len(s2) <= len(s1):
            return False
        been2 = Counter(s2[:len(s1)])
        l, r = 0, len(s1)
        while r < len(s2):
            been2[s2[r]] = been2.get(s2[r], 0) + 1
            r += 1
            been2[s2[l]] -= 1
            if been2[s2[l]] == 0:
                del been2[s2[l]]
            l += 1
            if been == been2:
                return True
        return False
            
            



        