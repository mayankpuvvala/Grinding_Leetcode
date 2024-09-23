# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1=None
        head2= head

        while head2!=None:
            head3= head2.next
            head2.next= head1
            head1= head2
            head2= head3
        return head1