# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current=dummy
        carry=0

        while l1 or l2 :
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            t_sum=val1+val2+carry


            carry=t_sum//10
            current.next=ListNode(t_sum%10)

            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry>0:
            current.next=ListNode(carry)
        
        return dummy.next

                


