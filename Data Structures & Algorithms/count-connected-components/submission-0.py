class DisjointSet:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, n):
        parent = self.parent[n]
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent

    def union(self, n1, n2):
        parent1, parent2 = self.find(n1), self.find(n2)
        if parent1 == parent2: return False

        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1
        
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DisjointSet(n)
        numberOfComponents = n
        for u, v in edges:
            if dsu.union(u, v):
                numberOfComponents -= 1
        return numberOfComponents

        