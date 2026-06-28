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
        self.heap[1] = self.heap.pop()
        i = 1
        while i * 2 < len(self.heap):
            left, right = i * 2, i * 2 + 1
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                if self.heap[i] > self.heap[right]:
                    self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                    i = right
                else:
                    break
            elif self.heap[left] < self.heap[i]:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            else:
                break
        return popped

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return arr
        self.heap = [None]
        ans = []
        for i in range(len(arr)):
            self.push((abs(x - arr[i]), arr[i]))
        for i in range(k):
            smallest = self.pop()
            ans.append(smallest[1])
        return sorted(ans)


        
        

                


