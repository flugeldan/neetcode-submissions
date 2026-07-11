import heapq
class Solution:
    def push(self, pair):
        self.heap.append(pair)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    
    def pop(self):
        if len(self.heap) == 2:
            return self.heap.pop()
        popped = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1 
        while i * 2 < len(self.heap):
            left, right = i * 2, i * 2 + 1
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                minChild = right
            else:
                minChild = left
            if self.heap[i] > self.heap[minChild]:
                self.heap[i], self.heap[minChild] = self.heap[minChild], self.heap[i]
                i = minChild
            else:
                break
        return popped



    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        self.heap = [None]
        for i, num in enumerate(nums):
            self.push((num, i))
        for _ in range(k):
            pair = self.pop()
            nums[pair[1]] = pair[0] * multiplier
            self.push((nums[pair[1]], pair[1]))
        return nums
        

