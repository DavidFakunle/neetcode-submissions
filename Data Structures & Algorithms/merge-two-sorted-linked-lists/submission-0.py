# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand- given heads ot two sorted lists merge the two lists into one
            input - two sorted list
            output - one merged sorted list
        Plan-
            merge list1 and list2 into list 1

            start with dummy node
            set curr to dummy
            
            loop while list1 and list 2 is available 
            check if list 1 value is less then list 2 value 
                if true set curr.next to list1
                and move on to the nex value in list1
            otherwise
                set curr.next to list2 value
                and move on to next value in list2

            move current to the next one


            then check after the loop if lists is empty 
            if notadd them respectively 


            then return dummy.next since dummy head was just a place holder
        Implement-
        '''


        dummy = ListNode(0)

        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next


        
        #this is for if one list is longer than other
        if not list1:
            curr.next = list2 # if list1 empty add list 2 remaining values
        else:
            curr.next = list1


        return dummy.next 