# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def recursivePostorderTraversal(root):
            if not root: return
            recursivePostorderTraversal(root.left)
            recursivePostorderTraversal(root.right)
            result.append(root.val)

        recursivePostorderTraversal(root)

        return result