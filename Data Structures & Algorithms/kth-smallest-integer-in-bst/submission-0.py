# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Understand- given a binary search tree return the kth smallest value
        Plan-
            Using inorder traversal this gives you the sorted order( from least to greatest) for free
            then return result[k] 
        Implement-
        '''
        result = []

        def inorder(node):
            if not node:
                return []

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        return result[k - 1]
        