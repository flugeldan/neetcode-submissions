class Solution:
    def find(self, n):
        root = n
        while root != self.par[root]:
            root = self.par[root]
        cur = n
        while cur != self.par[cur]:
            nxt = self.par[cur]
            self.par[cur] = root
            cur = nxt
        return root
            
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True
        
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.rank, self.par = {}, {}
        ans = 0
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        for edge in edges:
            self.union(edge[0], edge[1])
        for key, val in self.par.items():
            if key == val:
                ans += 1 

        return ans


        


        