class MyCircularQueue:
    def __init__(self, k: int):
        # k 크기의 원형 큐로 사용할 배열 선언
        self.q = [0] * k
        self.front = 0
        self.rear = -1
        self.len = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        # 꽉 차 있지 않다면 삽입 진행
        if not self.isFull():
            # rear 포인터 한 칸 앞으로 이동, 최대 크기를 초과하면 나머지 위치로 이동
            self.rear = (self.rear + 1) % self.size
            # rear 위치에 값 삽입
            self.q[self.rear] = value
            # 현재 큐의 크기 계산
            self.len += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        # 텅 비어 있지 않다면 삭제 진행
        if not self.isEmpty():
            # front 포인터 한 칸 앞으로 이동, 최대 크기를 초과하면 나머지 위치로 이동
            self.front = (self.front + 1) % self.size
            # 현재 큐의 크기 계산
            self.len -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        # 맨 앞의 값을 가져온다.
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        # 맨 뒤의 값을 가져온다.
        return -1 if self.isEmpty() else self.q[self.rear]

    def isEmpty(self) -> bool:
        # 현재 큐의 크기가 0이면 비어 있음
        return self.len == 0

    def isFull(self) -> bool:
        # 현재 큐의 크기가 전체 큐의 크기와 일치하면 꽉 차 있음
        return self.len == self.size


# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4

# [null, null, null, 1, 1, false]
input1 = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
input2 = [[3], [1], [2], [3], [4], [], [], [], [4], []]
myCircularQueue = MyCircularQueue(3);
# True
print(myCircularQueue.enQueue(1))
# True
print(myCircularQueue.enQueue(2))
# True
print(myCircularQueue.enQueue(3))
# False
print(myCircularQueue.enQueue(4))
# 3
print(myCircularQueue.Rear())
# True
print(myCircularQueue.isFull())
# True
print(myCircularQueue.deQueue())
# True
print(myCircularQueue.enQueue(4))
# 4
print(myCircularQueue.Rear())
