# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand- given a single linked list, reverse the list and return the new list
            input - linked list 
            output - reversed linked list
        Plan-
        example:
            0 -> 1 -> 2 -> 3

        if linked list empty 
            return empty list

        curr = head
        prev = null 


        Implement-
        '''

        prev , curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
