class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# [null, null, null, 2, 2, false]
input1 = ["MyStack", "push", "push", "top", "pop", "empty"]
input2 = [[], [1], [2], [], [], []]
obj = MyStack()
print(obj.push(1))
print(obj.push(2))
print(obj.top())
print(obj.pop())
print(obj.empty())
