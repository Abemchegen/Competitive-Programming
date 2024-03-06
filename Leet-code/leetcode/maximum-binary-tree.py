# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        print(nums)

        def design(nums):

            if not nums:
                return None

            maxind = nums.index(max(nums))
            left = design(nums[:maxind])
            right = design(nums[maxind+1:])
           
            return TreeNode(nums[maxind], left, right)

        return design(nums)


        