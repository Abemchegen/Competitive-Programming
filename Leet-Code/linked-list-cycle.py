# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head:

            slow = head
            fast = head
            flag = False

            while fast.next != None and fast.next.next != None:

                flag = True

                fast=fast.next.next
                slow=slow.next

                if fast == slow :

                    break
            if flag:

                slow = head

                while fast.next and slow.next:

                    slow=slow.next
                    fast=fast.next

                    if fast == slow:
                        return True

        return False

        