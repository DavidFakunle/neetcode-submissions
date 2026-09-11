# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Understand- Given two binary trees rebuild the binary tree from the preorder and inorder 
        traversals and return the root
        Plan-
        start off the new array using the root of the        preorder traversal
        find the that values position in inorder , and the position of inorder splits the array cleanly   
        the left side from the mid is the left side of the tree
        the right side from the mide is the right side of the tree
        Implement-
        '''

        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = idx_map[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
        