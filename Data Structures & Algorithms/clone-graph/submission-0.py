"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        old_to_new = {}

        stack = [node]
        visited = set()
        visited.add(node)

        while stack:
            curr = stack.pop()
            old_to_new[curr] = Node(val=curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        
        stack = [node]
        visited = set()
        visited.add(node)

        while stack:
            curr = stack.pop()
            for neighbor in curr.neighbors:
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return old_to_new[node]

