# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumn(root, ans):

            if not root:
                return 0

            if not root.left and not root.right:
                temp = ans + [str(root.val)]
                return int( "".join(temp))

            ans.append(str(root.val))
            l = r = out = 0

            if root.left:

                l = sumn(root.left, ans)
        
                print(l, root.val, "l")
                print(ans)        

            if root.right:

                r = sumn(root.right, ans)
                
                print(r, root.val,"r")
                print(ans)        


            out += l + r
            ans.pop()

            return out

        return sumn(root, [])




        

        