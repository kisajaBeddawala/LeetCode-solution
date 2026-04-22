# Path Sum II

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        def dfs(root,targetSum,l):
            if not root.left and not root.right:
                if  targetSum == 0:
                    ans.append(l[:])
                    l.pop()
                else:
                    l.pop()
                return
  
            if root.left:
                l.append(root.left.val)
                dfs(root.left,targetSum-root.left.val,l)
            if root.right:
                l.append(root.right.val)
                dfs(root.right,targetSum-root.right.val,l)
            # print(l,root.val)
            l.pop()
        dfs(root,targetSum-root.val,[root.val])

        return ans

