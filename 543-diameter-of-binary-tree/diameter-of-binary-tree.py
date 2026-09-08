# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0

        def height(node):
            if node == None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            self.diameter = max(self.diameter,leftHeight + rightHeight)

            return 1 +max(leftHeight, rightHeight)

        height(root)
        return self.diameter