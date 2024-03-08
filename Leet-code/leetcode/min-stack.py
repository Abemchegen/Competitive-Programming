class MinStack:

    def __init__(self):

        self.st = []
        self.temp = []

    def push(self, val: int) -> None:

        if not self.temp or val <= self.temp[-1]:
            
            self.temp.append(val)

        self.st.append(val)
        
    def pop(self) -> None:

        val = self.st.pop()

        if val == self.temp[-1]:
            self.temp.pop()

    def top(self) -> int:

        return self.st[-1]

    def getMin(self) -> int:
        return self.temp[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()