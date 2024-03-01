# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        queue = deque()
        queue.appendleft(root)
        ans = []

        while queue:

            a = []
            for i in range(len(queue)-1, -1, -1 ):
                a.append(queue[i].val)
            ans.append(a)
            
            for i in range(len(queue)):

                temp = queue.pop()

                if temp.left:
                    queue.appendleft(temp.left)

                if temp.right:
                    queue.appendleft(temp.right)


        for i in range(len(ans)):

            if i % 2 != 0:
                ans[i].reverse()
        return ans