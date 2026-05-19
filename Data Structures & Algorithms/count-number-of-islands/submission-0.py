class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for i_offset, j_offset in offsets:
                    dfs(i+i_offset, j+j_offset)

        number_of_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    dfs(i, j)

        return number_of_islands