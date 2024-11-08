# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast= head
        mid=0
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
            mid+=1
        prev= None
        temp= head
        while mid:
            front= temp.next
            temp.next= prev
            prev= temp
            temp= front
            mid-=1
        maxi= 0
        while slow and prev:
            maxi= max(maxi, prev.val+slow.val)
            prev =prev.next
            slow = slow.next
        return maxi