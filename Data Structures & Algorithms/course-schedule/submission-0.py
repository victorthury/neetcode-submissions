class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITING: return False
            elif state == VISITED: return True

            states[node] = VISITING

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            states[node] = VISITED
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True