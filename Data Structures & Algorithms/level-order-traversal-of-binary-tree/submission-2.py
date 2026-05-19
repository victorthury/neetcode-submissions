# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque()
        result = []

        queue.append(root)

        while queue:
            level_result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_result.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
            result.append(level_result)
        return result
