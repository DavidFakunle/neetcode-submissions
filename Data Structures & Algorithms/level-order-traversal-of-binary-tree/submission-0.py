# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Understand- Given a binary tree, return a list of each level of the binary  tree
        input - binary tree
        output - a list fo the list of values of binary tree
        Plan-
            handle the edge case if the root is empty then return empty list
            use BFS to traverse 
            append each value of a level into a list
            then append that into the final result list
        Implement-
        '''
        from collections import deque

        if root is None:
            return []

        
        results = []
        queue = deque([root])


        while queue:
            level_size = len(queue)
            level_values = [] # this is to store values in the level

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)


            results.append(level_values)


        return results
