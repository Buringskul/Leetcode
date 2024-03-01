# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        
        curr = head
        num = []

        while curr:
            num.append(curr.val)
            curr = curr.next
        
        return num == num[::-1]