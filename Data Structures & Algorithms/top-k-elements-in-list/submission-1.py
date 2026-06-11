class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashcheck={}
        for num in nums:
            hashcheck[num]=hashcheck.get(num, 0)+1
        listofnums=sorted(hashcheck.items(), key=lambda x: x[1], reverse=True)
        top_k=[x[0] for x in listofnums[:k]]
        return top_k
        

        
        