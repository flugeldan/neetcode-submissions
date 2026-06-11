from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keystore=defaultdict(list)
        self.timestampstore=defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append(value)
        self.timestampstore[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore or timestamp < self.timestampstore[key][0]:
            return ""
        elif timestamp >= self.timestampstore[key][-1]:
            return self.keystore[key][-1]
        
        l,r=0,len(self.timestampstore[key])-1
        lastLower=-1
        while l<=r:
            mid=(l+r)//2
            if self.timestampstore[key][mid]==timestamp:
                return self.keystore[key][mid]
            elif self.timestampstore[key][mid] > timestamp:
                r=mid-1
            else:
                lastLower=mid
                l=mid+1
        return self.keystore[key][lastLower]
