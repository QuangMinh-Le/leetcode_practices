class MyStack:

    def __init__(self):
        self.mystack = []

    def push(self, x: int) -> None:
        self.mystack.append(x)

    def pop(self) -> int:
        return self.mystack.pop(-1)

    def top(self) -> int:
        return self.mystack[-1]

    def empty(self) -> bool:
        return len(self.mystack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()