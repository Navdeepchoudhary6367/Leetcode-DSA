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
        def solve(node):
            if node is None:
                return 0
            LH = solve(node.left)
            if LH == -1:
                return -1
            RH = solve(node.right)
            if RH == -1:
                return -1
            if abs(LH-RH)>1:
                return -1
            return 1 + max(LH,RH)

        x = solve(root)
        if x ==-1:
            return False
        return True