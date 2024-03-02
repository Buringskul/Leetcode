# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(val=0, next = head)
        prev = temp
        curr = prev.next
        
        while curr and prev:
            nextNode = curr.next
            if nextNode and curr.val == nextNode.val:
                
                while nextNode and curr.val == nextNode.val:
                    curr = curr.next
                    nextNode = nextNode.next
                    
                prev.next = nextNode
                curr = nextNode
                
            else:
                prev = curr
                curr = nextNode
                
        return temp.next