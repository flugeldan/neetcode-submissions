class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [None]
        
        while nums:
            x = nums.pop()
            heap.append(x)
            i = len(heap) - 1 
            while i > 1 and heap[i] < heap[i // 2]:
                heap[i], heap[i // 2] = heap[i // 2], heap[i]
                i = i // 2
        
        while len(heap) > k + 1:
            heap[1] = heap.pop()
            i = 1
            while i * 2 < len(heap):
                if i * 2 + 1 < len(heap):
                    left = i * 2 
                    right = i * 2 + 1 
                    minChild = left if heap[left] <= heap[right] else right

                    if heap[i] > heap[minChild]:
                        heap[i], heap[minChild] = heap[minChild], heap[i]
                        i = minChild
                    else:
                        break
                else:
                    if heap[i * 2] < heap[i]:
                        heap[i * 2], heap[i] = heap[i], heap[i * 2]
                        i *= 2 
                    else:
                        break
        return heap[1]
        