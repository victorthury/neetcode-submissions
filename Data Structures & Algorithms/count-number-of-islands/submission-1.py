class DSU:
    def __init__(self, n, m):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            for j in range(m):
                self.parent[(i, j)] = (i, j)
                self.rank[(i, j)] = 1

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv: return False

        if self.rank[pu] >= self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += 1
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1

        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows, cols)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    for dr, dc in directions:
                        next_r, next_c = i + dr, j + dc
                        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == "1":
                            if dsu.union((i, j), (next_r, next_c)):
                                islands -= 1

        return islands

        