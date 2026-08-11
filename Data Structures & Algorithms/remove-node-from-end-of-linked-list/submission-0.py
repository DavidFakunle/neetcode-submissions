# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Understand- remove nth node from the end of list and return the new list
            input - head , n
            output - the new node with the n'th node removed
        Plan-
        set a dummy head node 
        start two pointers, fast and slow
        move fast forward n + 1 steps
        then move fast and slow together , until fast hits none
        whenever fast hits none, this means we are on the node before the actual node we are deleting
        return new linked list 
        Implement
        '''

        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        
        while fast is not None:
            fast = fast.next
            slow = slow.next

        
        slow.next = slow.next.next

        return dummy.next