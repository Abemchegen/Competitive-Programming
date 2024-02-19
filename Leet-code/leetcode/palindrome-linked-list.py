# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next == None:
            return True
        elif head.next.next == None:
            t = head
            if t.val == t.next.val :
                return True
            else:
                return False

        fast = head 
        slow = head 

        while fast != None and fast.next != None :

            fast = fast.next.next

            slow = slow.next

        temp1 = slow.next
        temp2 = slow.next.next
        slow.next = None
        
        while slow and temp1:

            temp1.next = slow
            slow = temp1
            temp1 = temp2
            if temp2 == None:
                break
            temp2 = temp2.next

        print(slow.val)

        front = head
        back = slow 

        while front and back:

            if front.val != back.val :

                return False

            front = front.next
            back = back.next

        return True