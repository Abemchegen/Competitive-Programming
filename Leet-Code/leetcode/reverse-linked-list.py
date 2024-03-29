# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head==None or head.next == None:
            return head

        i=head
        j=head.next
        i.next = None

        while j != None:

            temp = j
            
            j = j.next

            temp.next=i

            i=temp

        return i


            

        