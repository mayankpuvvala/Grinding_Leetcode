class MyCircularQueue:

    def __init__(self, k: int):
        self.curr= deque()
        self.k= k

    def enQueue(self, value: int) -> bool:
        if len(self.curr)==self.k:
            return False
        self.curr.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.curr)==0:
            return False
        self.curr.popleft()
        return True

    def Front(self) -> int:
        return self.curr[0] if self.curr else -1

    def Rear(self) -> int:
        return self.curr[-1] if self.curr else -1

    def isEmpty(self) -> bool:
        return len(self.curr)==0

    def isFull(self) -> bool:
        return len(self.curr)==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()