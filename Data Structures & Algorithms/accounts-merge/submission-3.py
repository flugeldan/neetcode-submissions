from collections import defaultdict
class Solution:
    def find(self, n):
        root = cur = n
        while root != self.par[root]:
            root = self.par[root]
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

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.par, self.rank, owners, groups = {}, {}, {}, defaultdict(list)
        ans = []
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                self.par[accounts[i][j]] = accounts[i][j]
                self.rank[accounts[i][j]] = 0
                owners[accounts[i][j]] = accounts[i][0]

        for i in range(len(accounts)):
            for j in range(2, len(accounts[i])):
                self.union(accounts[i][j], accounts[i][j - 1])
        
        for child in self.par:
            groups[self.find(child)].append(child)
        
        for group in groups.values():
            group.sort()
            ans.append([owners[group[0]]] + group)
        return ans

        
        





        