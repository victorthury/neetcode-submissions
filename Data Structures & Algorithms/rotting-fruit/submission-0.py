from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        q = deque()

        m, n = len(grid), len(grid[0])
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh += 1

        if fresh == 0: return 0

        minutes_elapsed = -1

        while q:
            minutes_elapsed += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for i_offset, j_offset in offset:
                    r, c = i + i_offset, j + j_offset
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))

        if fresh: return -1
        
        return minutes_elapsed
        