from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans, heap, count = 0, [], Counter(tasks) 
        heapq.heapify(heap)
        for key, val in count.items():
            heapq.heappush(heap, [-val, key])
        while heap:
            temp = []
            for _ in range(n + 1):
                if not heap:
                    break
                temp.append(heapq.heappop(heap))
            
            length = len(temp)
            temp = [[freq + 1, char] for freq, char in temp if freq + 1 < 0]
            if temp:
                ans += n + 1
            else:
                ans += length
            while temp:
                heapq.heappush(heap, temp.pop())
        return ans
        