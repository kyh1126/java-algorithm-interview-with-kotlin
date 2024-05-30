class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        target = self.queue[0]
        self.queue = self.queue[1:]
        return target

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

# [null, null, null, 1, 1, false]
input1 = ["MyQueue", "push", "push", "peek", "pop", "empty"]
input2 = [[], [1], [2], [], [], []]
myQueue = MyQueue()
print(myQueue.push(1))
print(myQueue.push(2))
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
