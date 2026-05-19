from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic_queue = deque()
        atlantic_seen = set()

        pacific_queue = deque()
        pacific_seen = set()

        m, n = len(heights), len(heights[0])

        for j in range(n):
            pacific_queue.append((0, j))
            pacific_seen.add((0, j))
        
        for i in range(1, m):
            pacific_queue.append((i, 0))
            pacific_seen.add((i, 0))

        for i in range(m):
            atlantic_queue.append((i, n-1))
            atlantic_seen.add((i, n-1))

        for j in range(n-1):
            atlantic_queue.append((m-1, j))
            atlantic_seen.add((m-1, j))

        def get_coords(queue, seen):
            while queue:
                i, j = queue.popleft()
                for i_offset, j_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = i + i_offset, j + j_offset
                    if 0 <= row < m and 0 <= col < n and heights[row][col] >= heights[i][j] and (row, col) not in seen:
                        queue.append((row, col))
                        seen.add((row, col))       


        get_coords(pacific_queue, pacific_seen)
        get_coords(atlantic_queue, atlantic_seen)

        return list(pacific_seen.intersection(atlantic_seen))                 