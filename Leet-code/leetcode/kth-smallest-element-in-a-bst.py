# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        

        def dfs(root):

            ans = []
            if not root :
                return ans
            

            ans.extend(dfs(root.left))
            ans.append(root.val)
            ans.extend(dfs(root.right))

            return ans


        ans = dfs(root)
        return ans[k-1]

        


        
        