# Symmetric Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(left,right):
            if not left and not right:
                return True
            elif (not left and right) or (not right and left):
                return False
            else:
                if left.val != right.val:
                    return False
                return check(left.left, right.right) and check(left.right,right.left)

        if not root:
            return True
        else:
            return check(root.left, root.right)
        