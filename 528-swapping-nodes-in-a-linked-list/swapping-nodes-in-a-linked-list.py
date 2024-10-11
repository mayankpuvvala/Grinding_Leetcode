# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp= head
        count=0
        first=0

        while temp:
            count+=1
            if count==k:
                first= temp.val
            temp= temp.next
        
        second=0
        temp=head
        newt=0
        while temp:
            newt+=1
            if newt==count-k+1:
                second= temp.val
                temp.val= first
            temp=temp.next

        temp=head
        newt=0
        while temp:
            newt+=1
            if newt==k:
                temp.val=second
                break
            temp=temp.next
        return head

            



        