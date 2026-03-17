# Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return True
        
        # Function to find the height of the tree
        def findH(head):
            if not head:
                return 0
            lH = findH(head.left)
            rH = findH(head.right)

            return max(lH,rH) + 1

        leftH = 0
        rightH = 0
       
        leftH = findH(root.left)
        rightH = findH(root.right)

        # check tree is balanced or not
        if abs(rightH - leftH) > 1:
            return False
        
        # check for all the nodes in the tree if they are balanced or not
        return self.isBalanced(root.left) and self.isBalanced(root.right)