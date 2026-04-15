class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if self.stack == [] :
            self.mins.append(val)
        else :
            if self.mins[-1] >= val :
                self.mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.mins[-1] == self.stack[-1] :
            self.mins.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 1 :
            self.min = self.stack[-1] 
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
