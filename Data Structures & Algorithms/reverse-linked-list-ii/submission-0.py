# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head

        for _ in range(left-1):
            prev = prev.next
        
        curr = prev.next
        left_node = curr
        rev_prev = None

        for _ in range(right-left+1):
            nxt = curr.next
            curr.next = rev_prev
            rev_prev = curr
            curr = nxt

        prev.next = rev_prev
        left_node.next = curr
    
        return dummy.next
