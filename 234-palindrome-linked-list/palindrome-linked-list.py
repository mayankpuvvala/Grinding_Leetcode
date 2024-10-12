# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count= 0
        temp= head

        while temp:
            count+=1
            temp=temp.next
        
        newt= count//2
        
        prev= None
        temp= head

        while newt>0:
            front= temp.next
            temp.next= prev
            prev= temp
            temp= front
            newt-=1

        
        if count%2!=0:
            temp= temp.next
        
        while temp and prev:
            if not temp or not prev or temp.val!=prev.val:
                return False

            else:
                temp= temp.next
                prev= prev.next
        return True
            
