# Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        answer = []
        def inOrder(head):
            if head == None:
                return
            inOrder(head.left)
            answer.append(head.val)
            inOrder(head.right)
        
        inOrder(root)
        return answer




        