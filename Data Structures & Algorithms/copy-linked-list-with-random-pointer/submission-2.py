"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}

        curr = head

        while curr:
            old_to_new[curr] = Node(x= curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            old_to_new[curr].next = old_to_new[curr.next] if curr.next else None
            old_to_new[curr].random = old_to_new[curr.random] if curr.random else None
            curr = curr.next
        
        return old_to_new[head]