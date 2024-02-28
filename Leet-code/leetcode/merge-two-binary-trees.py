# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None

        if root1 and root2:

            root1.val += root2.val

        elif not root1 and root2:
            root1 = TreeNode(root2.val)

            if root2:
             root1.left = self.mergeTrees(root1.left, root2.left)

            if root2:
                root1.right = self.mergeTrees(root1.right, root2.right)

            return root1

        if root2:
            root1.left = self.mergeTrees(root1.left, root2.left)

        if root2:
            root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

        


            

        
 



        