# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:



        def check(temp1, temp2):

            if not temp1 and not temp2:
                return True
            elif temp1 and temp2 and temp1.val == temp2.val:
                return check(temp1.left, temp2.right) and check(temp1.right , temp2.left)
            else:
                return False

        return check(root.left, root.right)
        