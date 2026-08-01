class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        shortest = min(strs, key=len, default="")
        for i, char in enumerate(shortest):
            if all(string[i] == char for string in strs):
                ans += char
            else:
                break
        return ans

        