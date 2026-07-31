class MedianFinder:

    def __init__(self):
        self.cur = 0
        self.first, self.second = [], [] #first is max heap, second is min_heap
        self.one = True
        heapq.heapify(self.first)
        heapq.heapify(self.second)
        

    def addNum(self, num: int) -> None:
        if self.first and not self.second:
            heapq.heappush(self.second, num)
            return
        heapq.heappush(self.first, -num)
        while self.second and -self.first[0] > self.second[0]:
            if self.second:
                head_second = heapq.heappop(self.second)
                heapq.heappush(self.first, -head_second)
            head_first = -heapq.heappop(self.first)
            heapq.heappush(self.second, head_first)
        while self.first and len(self.first) - 1 > len(self.second):
            heapq.heappush(self.second, -heapq.heappop(self.first))
        
            


#if num < head of second part, pop head of second and add as max of first 
#if num > head of first, pop head of first, put it into second, it will be minimal
#all elements in first should be <= elements of second
#head of first should be <= head of second
#i need to somehow guarantee that all elements in max heap (first half of the array) will be <= all elements second part of the array (min heap), if i will be able to do that i will be able to do just (-self.first[0] + self.second[0]) / 2 or just -self.first[0]

    def findMedian(self) -> float:
        if len(self.first) == len(self.second):
            return (-self.first[0] + self.second[0]) / 2
        else:
            return -self.first[0]
    
        
        