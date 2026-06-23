import math
from collections import defaultdict
class Solution:
    def push(self, val):
        self.heap.append(val)
    
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

        
    def pop(self):
        if len(self.heap) == 2:
            return self.heap.pop()
        popped = self.heap[1]
        i = 1
        self.heap[1] = self.heap.pop()

        while i * 2 < len(self.heap):
            left, right = i * 2, i * 2 + 1
            minChild = None
            if right < len(self.heap) and self.heap[right] <= self.heap[left]:
                minChild = right
            else:
                minChild = left
            if self.heap[i] > self.heap[minChild]:
                self.heap[i], self.heap[minChild] = self.heap[minChild], self.heap[i]
                i = minChild
            else:
                break
        return popped

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = [None]
        self.k = k
        check = defaultdict(list)
        ans = []
 
        for point in points:
            key = point[0] ** 2 + point[1] ** 2
            check[key].append(point[0])
            check[key].append(point[1])
            self.push(key)

        
        for _ in range(k):
            x = self.pop()
            y = check[x].pop()
            x = check[x].pop()
            ans.append([x, y])
            



     
 

        return ans

        