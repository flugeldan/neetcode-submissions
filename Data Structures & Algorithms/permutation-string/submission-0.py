from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        letters1=Counter(s1)
        letters2={}
        for i in range(len(s1)):
            letters2[s2[i]]=letters2.get(s2[i],0)+1
        if letters1==letters2:
            return True
        for r in range(len(s1),len(s2)):
            if letters2==letters1:
                return True
            left=r-len(s1)
            letters2[s2[left]]-=1
            if letters2[s2[left]]==0:
                del letters2[s2[left]]
            left+=1
            letters2[s2[r]]=letters2.get(s2[r],0)+1
            if letters2==letters1:
                return True

        return False

        
        