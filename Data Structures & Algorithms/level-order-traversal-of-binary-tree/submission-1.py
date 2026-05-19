# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        queue = collections.deque()

        queue.append(root)

        while queue:
            queueLen = len(queue)
            level = []
            for i in range(queueLen):
                element = queue.popleft()
                if element:
                    level.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
            if level:
                levels.append(level)
        return levels