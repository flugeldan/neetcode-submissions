import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_in=max(piles)
        if h==len(piles):
            k=max_in
            return k
        l,r=1, max_in
        while l<r:
            mid=(l+r)//2
            totalhours=0
            for pile in piles:
                totalhours+=math.ceil(pile/mid)
            if totalhours> h:
                l=mid+1
            else:
                r=mid
        return l


            





            
            


            


        