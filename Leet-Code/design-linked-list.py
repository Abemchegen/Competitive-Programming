class node:

    def __init__(self, data):
        self.data=data
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.dummy = node(0)
        self.size = 1
        
    def get(self, index: int) -> int:

        if index >= self.size - 1 :
            return -1

        temp = self.dummy

        while index + 1 :
            temp=temp.next
            index -= 1

        return temp.data

    def addAtHead(self, val: int) -> None:

        newnode = node(val)
        newnode.next = self.dummy.next
        self.dummy.next = newnode
        self.size+=1

    def addAtTail(self, val: int) -> None:

        newnode = node(val)
        temp = self.dummy

        while temp.next:
            temp=temp.next

        temp.next=newnode 
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size -1  :
            return
          
        newnode = node(val)
        temp= self.dummy

        c=0

        while c < index :

            temp=temp.next
            c+=1

        newnode.next = temp.next
        temp.next=newnode 

        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        
        if index >= self.size - 1:
            return 

        temp = self.dummy
        c=0

        while c < index :

            temp= temp.next
            c+=1

        if index == self.size - 2:
            temp.next=None

        else:
            temp.next=temp.next.next
            
        self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)