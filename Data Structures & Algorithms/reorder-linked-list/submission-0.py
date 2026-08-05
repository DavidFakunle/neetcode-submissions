# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Understand- given a list of values reorder it in this order[0, n-1, 1, n-2, 2, n-3, ...]
            input - head of node
            output - no output just modify in place
        Plan-
            take the beginging of the list and merge it with second half in alternating way
            reverse the second half of the list 
            then merge alternatively 

            to find middle 
            set slow pointer to first node
            fast pointer to second node
            move both pointers till fast reaches end, meaning slow is at halfway point 
            then slow.next = 2nd half # even num of node
            last node point at null
        Implement-
        '''
        slow, fast = head, head.next

        while fast and fast.next: # to find middle 
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        prev = slow.next = None

        # reversing second half 
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp


        # merge two halfs

        first, second = head, prev 

        while second:
            tmp1, tmp2 = first.next , second.next # store it early 
            first.next = second
            second.next = tmp1
            first, second = tmp1 , tmp2

