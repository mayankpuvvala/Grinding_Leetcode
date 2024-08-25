"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newt= {None:None}

        curr= head
        while curr:
            newt[curr]= Node(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            copy= newt[curr]
            copy.next= newt[curr.next]
            copy.random= newt[curr.random]
            curr=curr.next
        return newt[head]