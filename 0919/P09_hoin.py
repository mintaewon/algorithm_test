# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None              
        while head:
            previous = newHead
            newHead = head          
            head = head.next         
            newHead.next = previous 
        return newHead
