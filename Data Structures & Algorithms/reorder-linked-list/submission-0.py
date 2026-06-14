# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #tortoise and hare approach for fast and slow pointers
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        l1=head
        l2=slow.next
        slow.next=None

        prev=None
        curr=l2

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l2=prev

        while l2:
            dummyl1=l1.next
            dummyl2=l2.next

            l1.next = l2
            l2.next = dummyl1

            l1=dummyl1
            l2=dummyl2