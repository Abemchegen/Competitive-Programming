# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p and q:

            if p.val == q.val :

                if self.isSameTree(p.left, q.left):
                    return self.isSameTree(p.right, q.right)
                else:
                    return False

            else :

                return False

        else:
            if not p and not q:
                return True
            else:
                return False



        