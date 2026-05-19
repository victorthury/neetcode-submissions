class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] and (i, j) not in visited:
                visited.add((i, j))            
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            else:
                return 0
    
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                maxArea = max(maxArea, dfs(i, j))
        return maxArea