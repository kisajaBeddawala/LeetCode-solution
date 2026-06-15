# Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def dfs(root,ans):
            if not root:
                return
            ans.append(root.val)
            dfs(root.left,ans)
            dfs(root.right,ans)

        ans = []
        dfs(root,ans)

        return ans

        