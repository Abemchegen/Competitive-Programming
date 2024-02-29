# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def maxan(root, maxval, minval, maxdiff):
            

            if not root:
                return maxdiff

            maxval = max(maxval, root.val)
            minval = min(minval, root.val)
            maxdiff = max(maxdiff, maxval - minval)
            maxdiff = maxan(root.left, maxval, minval, maxdiff)
            maxdiff = maxan(root.right, maxval, minval, maxdiff)

            return maxdiff
        
        return maxan(root, root.val, root.val, 0)
        