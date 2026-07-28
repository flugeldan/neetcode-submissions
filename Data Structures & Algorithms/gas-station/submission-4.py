class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        ans = -1
        i = 0
        while i < n:
            if tank == 0:
                tank = gas[i] 
            if tank < cost[i]:
                tank = 0
                i += 1 
                continue
            run = 0
            skip = False
            for j in range(i, n):
                run += gas[j]
                if run < cost[j]:
                    skip = True
                    i = j + 1
                    tank = 0
                    break
                run -= cost[j]
            if skip:  
                continue
            for j in range(i):
                run += gas[j]
                if run < cost[j]:
                    skip = True
                    tank = 0
                    break
                run -= cost[j]
            if not skip:
                ans = i
                break
            else:

                i += 1
        
        return ans


                
            
        