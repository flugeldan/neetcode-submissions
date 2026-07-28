class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        ans = -1
        for i in range(n):
            if tank == 0:
                tank = gas[i]
            if tank < cost[i]:
                tank = 0
                continue
            run = 0
            skip = False
            for j in range(i, n):
                run += gas[j]
                if run < cost[j]:
                    skip = True
                    break
                run -= cost[j]
            if skip:
                tank = 0
                continue
            for j in range(i):
                run += gas[j]
                if run < cost[j]:
                    skip = True
                    break
                run -= cost[j]
            if not skip:
                ans = i
                break

            
            
                
        
        return ans


                
            
        