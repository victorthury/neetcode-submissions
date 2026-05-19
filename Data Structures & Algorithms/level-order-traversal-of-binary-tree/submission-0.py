# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}

        def dfs(node, height):
            if node is None:
                return

            if height in levels:
                levels[height].append(node.val)
            else:
                levels[height] = [node.val]
            
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
        
        dfs(root, 0)
        return list(levels.values())