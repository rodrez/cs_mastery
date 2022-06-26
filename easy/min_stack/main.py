class MinStack:


    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.min_stack.append(val if not self.stack or val < self.stack[-1] else self.stack[-1])
        return self.stack.append(int)

    def pop(self) -> None:
        return self.stack.pop(self.stack[-1])

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(-11)
obj.push(1)
obj.push(12)
# obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3, param_4)