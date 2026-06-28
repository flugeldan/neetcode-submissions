from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        been = set()
        count = 0
        for pr in prerequisites:
            if (pr[1], pr[0]) in been:
                return False
            graph[pr[0]].append(pr[1])
            been.add((pr[0], pr[1]))
        
        cycle = False
        been, curBeen = set(), set()

        def dfs(i):
            nonlocal cycle
            if cycle:
                return
            if i in curBeen:
                cycle = True
                return
            if i in been:
                return
            curBeen.add(i)
            for preq in graph[i]:
                dfs(preq)
                if cycle:
                    return
            been.add(i)
            curBeen.remove(i)
        
        for c in range(numCourses):
            if c not in been:
                dfs(c)
                if cycle:
                    return False
        
        return True


        

        


        
        




        