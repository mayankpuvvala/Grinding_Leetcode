# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        temp=head
        first= None

        while left>1:
            first= temp
            temp=temp.next
            left-=1
            right-=1
        
        connection= first
        tail= temp

        prev= None
        while right>0:
            front= temp.next
            temp.next= prev
            prev= temp
            temp=front
            right-=1
        
        if connection:
            connection.next= prev
        else:
            head= prev
        
        tail.next= temp
        return head
