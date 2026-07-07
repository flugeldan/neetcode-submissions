from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odd = 0
        ans = 0
        for count in c:
            if c[count] % 2 == 0:
                ans += c[count]
            elif c[count] % 2 == 1:
                odd = 1
                ans += c[count] - 1

        ans += 1 if odd > 0 else 0
        return ans
