# Binary Tree Level Order Traversal II

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans = []
        queue = deque([root])
        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            ans.append(temp)

        ans.reverse()
        return ans
