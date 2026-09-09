# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Understand- return true if a treee is a valid binary tree meaning 
            the left values are less than the root and the right values are greater 
            than the root
            input - binary tree
            output - true if its valid, false if not
        Plan-
            Recursion
            in an helper function
                set the base case 
                if tree empty return true
                check the current node against the bounds 

                The rules of left subtree
                    all values must be less then node.val
                    but still respect the existing lower bound
                
                The rule of right subtree
                    all values must be greater than node.val
                    but still respect the upper bound 
                
                return by calling the function on its self checking both sides

            return the validate function with root and the upper and lower bounds 
                as neg infinity and pos infinity
        Implement-
        '''

        def validate(node, low, high):
            if not node:
                return True

            
            if not (low < node.val < high):
                return False


            return(validate(node.left, low, node.val) and validate(node.right, node.val, high))


        return validate(root, float('-inf'), float('inf'))
        