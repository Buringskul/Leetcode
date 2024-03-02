# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        temp = ListNode(0, next = head)
        prev = temp
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            first.next = second.next
            second.next = first
            
            prev.next = second
            prev = first
            
        return temp.next