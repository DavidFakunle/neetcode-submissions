# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Understand- given the roots of two binary return true if there is a subtree of root with the same strucure and node of subroot
        Plan-
        create an helper function sameTree to check if trees are equal 
        check if same Tree from root node 
        if not check from the left and right nodes

        if both trees are null
            return True 
        if main tree is empty and subtree isnt 
            return False 
        if subtree is empty and main tree isnt
            return True
        Implement
        '''

        if not subRoot: return True

        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.right, subRoot) or                
                    self.isSubtree(root.left,subRoot)) 
    def sameTree(self, s, t):
        if not s and not t:
            return True 

        if s and t and s.val == t.val: # comparing the trees 
            return (self.sameTree(s.left, t.left) and 
            self.sameTree(s.right, t.right)) 


        return False # if one is empty 

        
         