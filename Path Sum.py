# Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root,tot):
            if not root.left and not root.right:
                if tot == 0:
                    return True
                return False

            x = False
            y = False
            if root.left:
                x = dfs(root.left,tot-root.left.val) 
            if root.right:
                y = dfs(root.right,tot-root.right.val)

            return x or y
            
        if not root:
            return False
        
        return dfs(root,targetSum-root.val)
        