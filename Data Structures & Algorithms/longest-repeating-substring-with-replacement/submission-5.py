class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        max_length = 0
        l = 0
        max_freq=0
        for i in range(len(s)):
            frequency[s[i]]=frequency.get(s[i], 0)+1
            window_size=i-l+1
            max_freq=max(max_freq,frequency.get(s[i],0))
            while window_size-max_freq >k:
                frequency[s[l]]-=1
                l+=1
                max_freq=max(frequency.values())
                window_size=i-l+1
            max_length=max(max_length,i-l+1)
        return max_length

            