# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next= head
        slow, fast= head, head
        count=0
        while fast and fast.next:
            count+=1
            slow=slow.next
            fast= fast.next.next
        if fast:
            slow =slow.next
        prev= None
        while slow:
            front= slow.next
            slow.next= prev
            prev= slow
            slow= front
        while prev:
            if prev.val!=dummy.next.val:
                return False
            prev= prev.next
            dummy= dummy.next
        return True


        
