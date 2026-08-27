# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Understand- Swap the values of a binary tree, swap the left child with 
        the right child
            input - the normal binary tree
            output - the inverted binary tree
        Plan-
            create an helper function that swaps the node then return the helper function with the root 
        Implement-
        '''

        def swapValues(root):

            if root is None: # this checks if the root is empty
                return None 

            
            root.right, root.left = root.left, root.right # this swaps them.

            root.left = swapValues(root.left)
            root.right = swapValues(root.right)

            return root

        return swapValues(root) #Time: O(N) Space: O(h)