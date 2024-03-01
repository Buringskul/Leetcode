# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        address = set()
        curr = head
        while curr:
            if id(curr) not in address:
                address.add(id(curr))
                
            else:
                return curr
            
            curr = curr.next
            
        return None