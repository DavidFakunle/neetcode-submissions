# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Understand- Given a binary tree, and two nodes from the tree is p and q, return the lowest common ancestor of two nodes 
        Plan-
        if one node is greater than the root node, and the other is less then the lca is the root node

        Implement-
        '''

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val: # if both values greater look in right subtree
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: # else if both are left go down left subtree
                curr = curr.left
            else: # if we find any of the values p or q then we can return curr
                return curr

        