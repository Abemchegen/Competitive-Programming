# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        def bst(nums):

            if not nums:
                return None

            i = len(nums) // 2

            left = bst(nums[:i])
            right = bst(nums[i+1:])

            return TreeNode(nums[i], left, right)


        return bst(nums)