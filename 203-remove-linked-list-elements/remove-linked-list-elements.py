# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next = head
        temp = dummy

        while temp.next:
            if temp.next and temp.next.val!=val:
                temp= temp.next
            else:
                temp.next= temp.next.next
        return dummy.next