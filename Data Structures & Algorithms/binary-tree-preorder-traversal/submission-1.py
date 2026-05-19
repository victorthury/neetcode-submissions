# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def recursivePreorderTraversal(root):
            if not root: return

            result.append(root.val)
            recursivePreorderTraversal(root.left)
            recursivePreorderTraversal(root.right)
        
        recursivePreorderTraversal(root)

        return result
