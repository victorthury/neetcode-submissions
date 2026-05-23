class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.numberOfComponents = n

        for i in range (n):
            self.parent[i] = i
            self.rank[i] = 1 

    def find(self, x: int) -> int:
        parent = self.parent[x]
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent

    def isSameComponent(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        return px == py

    def union(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return False

        rankx = self.rank[px]
        ranky = self.rank[py]

        if rankx > ranky:
            self.parent[py] = px
        elif rankx < ranky:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        self.numberOfComponents -= 1

        return True

    def getNumComponents(self) -> int:
        return self.numberOfComponents

