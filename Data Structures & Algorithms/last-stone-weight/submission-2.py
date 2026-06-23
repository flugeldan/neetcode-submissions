class Solution:
    def pop(self):


        popped = self.heap[1]
        if len(self.heap) == 2:
            return self.heap.pop()
        self.heap[1] = self.heap.pop()
        i = 1 
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap):
                right = i * 2 + 1
                left = i * 2
                if self.heap[left] >= self.heap[right]:
                    maxChild = left
                else:
                    maxChild = right

                if self.heap[i] < self.heap[maxChild]:
                    self.heap[i], self.heap[maxChild] = self.heap[maxChild], self.heap[i]
                    i = maxChild
                else:
                    break
            else:
                if self.heap[i] < self.heap[i * 2]:
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                    i *= 2 
                else:
                    break
        return popped
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
        
        
        


    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [None]
        self.heap = heap
        for num in stones:
            self.push(num)
        
        while self.heap:
            if len(self.heap) == 1:
                return 0
            elif len(self.heap) == 2:
                return self.heap[1]
            
            a = self.pop()
            b = self.pop()
            if b < a:
                self.push(a - b)
                        

            









        