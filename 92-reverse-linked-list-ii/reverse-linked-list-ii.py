# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next = head
        prev_left= dummy

        for _ in range(left-1):
            prev_left= prev_left.next

        prev= None
        curr= prev_left.next
        newt= curr

        right= right - left + 1
        while right:
            front= newt.next
            newt.next= prev
            prev= newt
            newt= front
            right-=1
            
        prev_left.next= prev
        curr.next= newt
        
        return dummy.next