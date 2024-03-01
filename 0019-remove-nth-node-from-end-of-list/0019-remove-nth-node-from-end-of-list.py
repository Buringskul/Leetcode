# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        curr = head
        count = 0
        
        while curr:
            count += 1
            curr = curr.next
        
        if n >= count:
            return head.next
        
        nth = count - n - 1
        curr = head
        
        while nth > 0:
            curr = curr.next
            nth -= 1
        
        curr.next = curr.next.next
        return head
        
        