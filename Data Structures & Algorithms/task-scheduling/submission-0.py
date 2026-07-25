from collections import Counter
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        count = Counter(tasks)
        arr = []
        heapq.heapify(arr)
        for key, val in count.items():
            heapq.heappush(arr, [-val, key])
        while arr:
            temp = []
            for _ in range(n + 1):
                if not arr:
                    break
                temp.append(heapq.heappop(arr))
            cur_length = len(temp)
            temp = [[freq + 1, char] for freq, char in temp if freq + 1 < 0]
            if temp:
                ans += n + 1
            else:
                ans += cur_length
            while temp:
                heapq.heappush(arr, temp.pop())
        return ans
    


            
                



        


            












        



        

                


        

        



        