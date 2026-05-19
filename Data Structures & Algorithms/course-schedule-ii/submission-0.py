class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2

        states = [0] * numCourses

        coursesOrder = []

        def dfs(node):
            if states[node] == VISITING: return False
            if states[node] == VISITED: return True

            states[node] = VISITING

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            
            states[node] = VISITED
            coursesOrder.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return []
        return coursesOrder