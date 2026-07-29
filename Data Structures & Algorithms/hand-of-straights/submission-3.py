from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        count = Counter(hand)
        maxes = sorted(list(count))
        
        while count and maxes:
            if maxes[-1] not in count:
                maxes.pop()
                continue
            count[maxes[-1]] -= 1
            target = maxes[-1] - 1
            
            for _ in range(groupSize - 1):
                if target not in count:
                    return False
                count[target] -= 1
                if count[target] <= 0:
                    del count[target]
                target -= 1

            if count[maxes[-1]] <= 0:
                del count[maxes[-1]]
                maxes.pop()
            
        return True




        