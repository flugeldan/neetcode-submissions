from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tLetters=Counter(t)
        window={}
        l=0
        min_int=float('inf')
        res=""
        
        have=0
        need=len(tLetters)
        for i in range(len(s)):
            char=s[i]
            window[char]=window.get(char,0)+1
            if char in tLetters and window[char]==tLetters[char]:
                have+=1
            while have==need:
                if i-l+1 < min_int:
                    res=s[l:i+1]
                    min_int=i-l+1
                window[s[l]]-=1
                if s[l] in tLetters and window[s[l]]<tLetters[s[l]]:
                    have-=1
                l+=1
                
        return res




            

        
            





        