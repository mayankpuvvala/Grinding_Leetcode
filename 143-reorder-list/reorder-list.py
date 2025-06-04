# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        slow = head
        fast= head.next
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next

        prev= None
        curr= slow.next
        slow.next= None
        while curr:
            front= curr.next
            curr.next= prev
            prev= curr
            curr= front

        first,second= head, prev
        while second:
            tmp1, tmp2= first.next, second.next
            first.next= second
            second.next= tmp1
            first= tmp1
            second= tmp2
        
        return first