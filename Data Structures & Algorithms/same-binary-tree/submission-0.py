# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Understand- check both treees and return true if they are equal meaning they share the same structure and same values
        Plan-

        using recursion 
        set base cases for if both dont exist return ture
        base case: if one is missing return false

        if any value doesnt match up return False

        using recursion check both trees right and left values
        Implement-
        '''

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        
        if p.val != q.val:
            return False


        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)