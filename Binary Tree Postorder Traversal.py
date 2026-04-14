# Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def dfs(root,ans):
            if not root:
                return
            dfs(root.left,ans)
            dfs(root.right,ans)
            ans.append(root.val)

        ans = []
        dfs(root,ans)

        return ans