from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = defaultdict(list)

        for course, preq in prerequisites:
            if preq in graph and graph[preq] == course:
                return False
            graph[course].append(preq)
        
        been, curBeen = set(), set()
        cycle = False
        def dfs(c):
            nonlocal cycle
            if c in curBeen:
                cycle = True
                return
            if c not in graph:
                return
            curBeen.add(c)
            for preq in graph[c]:
                if preq not in been:
                    dfs(preq)
                if cycle:
                    return
            been.add(c)
            curBeen.remove(c)
        for key in graph:
            if key not in been:
                dfs(key)
                if cycle:
                    return False
        return True

        

        
        