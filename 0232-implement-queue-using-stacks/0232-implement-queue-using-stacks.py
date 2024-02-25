class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack1 and not self.stack2:
            self.stack1.append(x)
            self.stack2.append(x)
        else:
            self.stack1.append(x)
            self.stack2.insert(0, x)
        
    def pop(self) -> int:
        self.stack1.pop(0)
        return self.stack2.pop()

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()