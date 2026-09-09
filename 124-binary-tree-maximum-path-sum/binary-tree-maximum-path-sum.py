# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi = [float('-inf')]

        def solve(node):

            if node is None:
                return 0

            LS = solve(node.left)
            if LS<0:
                LS = 0
                
            RS = solve(node.right)
            if RS<0:
                RS = 0

            maxi[0] = max(maxi[0],LS+node.val+RS)

            return node.val+ max(LS,RS)

        solve(root)
        return maxi[0]