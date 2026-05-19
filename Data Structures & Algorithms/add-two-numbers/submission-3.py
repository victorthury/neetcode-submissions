# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carryOn = 0
        while l1 and l2:
            val = l1.val + l2.val + carryOn
            if val >= 10:
                carryOn = 1
                val = val - 10
            else:
                carryOn = 0
            
            newNode = ListNode(val=val)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = l1.val + carryOn
            if val >= 10:
                carryOn = 1
                val = val - 10
            else:
                carryOn = 0
            newNode = ListNode(val=val)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
        
        while l2:
            val = l2.val + carryOn
            if val >= 10:
                carryOn = 1
                val = val - 10
            else:
                carryOn = 0
            newNode = ListNode(val=val)
            curr.next = newNode
            curr = curr.next
            l2 = l2.next

        if carryOn:
            newNode = ListNode(val=carryOn)
            curr.next = newNode
        
        return dummy.next
            