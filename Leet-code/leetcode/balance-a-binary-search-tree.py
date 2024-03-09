# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:


        def traverse(root):

            arr = []

            if not root:
                return arr

            arr.extend(traverse(root.left))
            arr.append(root.val)
            arr.extend(traverse(root.right))

            return arr

        arr = traverse(root)

        def construct(nums):

            if not nums:
                return None

            i = len(nums) // 2

            left = construct(nums[:i])
            right = construct(nums[i+1:])

            return TreeNode(nums[i], left, right)

        return construct(arr)

        