# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Understand- traverse through the nodes and find the max depth of the binary tree
        Plan-
        using recursion 
        set the base case to 0 incase there is no root values

        then call the function on the left and right side

        return 1 + the deeper side using max (the one is there to include the first level)
        Implement-
        '''

        #using recursion

        if root is None:
            return 0


        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)

    
        return 1 + max(left_depth, right_depth)