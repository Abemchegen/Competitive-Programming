# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root):

            if not root.left and not root.right:

                return [root.val, root.val]

            a = b = []

            if root.left:

                a = valid(root.left)

            if root.right:

                b = valid(root.right)

            if ((not a) or (a and len(a) == 2 and root.val > a[1])) and ((not b) or (b and len(b) == 2 and root.val < b[0])):

                if a and b:

                    return [a[0],b[1]]

                elif not a and b:

                    return [root.val,b[1]]

                elif a and not b:

                    return [a[0],root.val]
            else:
                return [0, 0 , 0]

 
        if len(valid(root))== 2:
            return True
        else:
            return False




        
        