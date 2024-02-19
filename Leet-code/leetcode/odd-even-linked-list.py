# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None or head.next.next == None:
            return head

        temp = head 
        tail = None
        count = 1

        while temp.next :
            count += 1
            temp = temp.next
        
        tail = temp 
        temp = None

        start = head
        count = count // 2

        while count :

            mid = start.next
            start.next = mid.next
            tail.next = mid
            start = start.next
            tail = tail.next
            count -= 1

        tail.next = None

        return head


    
    