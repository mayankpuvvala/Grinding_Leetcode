# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow,fast= head,head

        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        ptr,prev= slow.next,None
        slow.next= None
        while ptr:
            front= ptr.next
            ptr.next= prev
            prev= ptr
            ptr= front

        head1,head2= head,prev
        while head2:
            front = head1.next
            head1.next=head2
            head1=head2
            head2= front
        
        