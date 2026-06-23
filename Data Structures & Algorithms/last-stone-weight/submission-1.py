class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-1], stones[-2] = stones[-2], stones[-1]
                stones[-2] = stones[-2] - stones[-1]
                
                stones.pop()
                stones.sort()
        return 0 if not stones else stones[0]



        