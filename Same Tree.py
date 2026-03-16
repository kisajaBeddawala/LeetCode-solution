# Same Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def check(l,r):
            if l == None and r == None:
                return True
            if not (l and r):
                return False
            if l.val != r.val:
                return False
            return check(l.left, r.left) and check(l.right, r.right)

        if p == None and q == None:
            return True
        if not (p and q):
            return False
        return check(p,q)
        
        