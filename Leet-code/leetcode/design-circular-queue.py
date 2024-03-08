class MyCircularQueue:

    def __init__(self, k: int):

        self.queue = [None] * k
        self.front = 0
        self.back = -1
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        
        if not self.isFull():

            self.back = (self.back + 1) % self.k
            self.queue[self.back] = value
            self.size += 1
            return True
        else:
            return False
        
    def deQueue(self) -> bool:

        if not self.isEmpty():
            self.front = (self.front + 1) % self.k
            self.size -= 1
            return True
        else:
            return False  
        
    def Front(self) -> int:

        if not self.isEmpty():
            return self.queue[self.front]
        else:
            return -1

    def Rear(self) -> int:

        if not self.isEmpty():
            return self.queue[self.back]
        else:
            return -1        

    def isEmpty(self) -> bool:

        if self.size == 0:
            return True
        else:
            return False
        
    def isFull(self) -> bool:

        if self.size >= self.k:
            return True
        else:
            return False
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()