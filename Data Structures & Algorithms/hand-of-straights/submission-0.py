from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        count = Counter(hand)
        while count:
            cur = max(count)
            count[cur] -= 1
            if count[cur] <= 0:
                del count[cur]
            target = cur - 1
            for _ in range(groupSize - 1):
                if target not in count:
                    return False
                count[target] -= 1
                if count[target] <= 0:
                    del count[target]
                target -= 1
        return True




        