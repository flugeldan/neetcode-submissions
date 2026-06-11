import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        bananas = sum(piles)
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            totalToEat = sum(math.ceil(x/mid) for x in piles) #сколько часов с нынешним rate нужно для того чтобы съесть все бананы

            if totalToEat > h:
                left = mid + 1
            else:
                right = mid
        return left #когда он достигнет правой то чаще всего он будет как раз и на минимально допустимом значении поедания бананов



                

