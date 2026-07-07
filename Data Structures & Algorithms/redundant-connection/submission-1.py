class Solution:
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        self.par[n] = p
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1 
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.par, self.rank = {}, {}
        for i in range(1, len(edges) + 1):
            self.par[i] = i
            self.rank[i] = 0
        ans = None
        for edge in edges:
            unified = self.union(edge[0], edge[1])
            if not unified:
                ans = edge
                
        
        return ans

        

        


        