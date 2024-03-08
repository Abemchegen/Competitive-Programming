# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        d = defaultdict(int)

        def traverse(temp):

            if not temp:
                return 

            d[temp.val] += 1
            traverse(temp.left)
            traverse(temp.right)

        traverse(root)
        maxi = max(d, key = lambda x : d.get(x))
        ans = []

        for i in d :

            if d[i] == d[maxi]:
               

                ans.append(i)

        return ans





        