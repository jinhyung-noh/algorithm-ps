class MyStack:
    def __init__(self):
        # push to back : list.insert(0, element)
        # pop form the front : list.pop()
        self.main_queue = []
        self.sub_queue = []

    def push(self, x: int) -> None:
        # move all element in main queue to sub queue
        while self.main_queue:
            self.sub_queue.insert(0, self.main_queue.pop())
        # push to back new element to main queue
        self.main_queue.insert(0, x)
        # move all elemnt in sub queue to main queue
        while self.sub_queue:
            self.main_queue.insert(0, self.sub_queue.pop())
        return None

    def pop(self) -> int:
        return self.main_queue.pop()

    def top(self) -> int:
        try:
            return self.main_queue[-1]
        except:
            return None

    def empty(self) -> bool:
        return len(self.main_queue) == 0


# solution in Book
class MyStack2:
    from collections import deque
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        # rearrange
        for _ in range(len(self.q-1)):
            self.q.append(self.q.popleft())

        def popo(self):
            return self.q.popleft()

        def top(self):
            return self.q[0]

        def empty(self):
            return len(self.q) == 0


stack1 = MyStack()
stack1.push(1)
stack1.push(2)
print(stack1.main_queue)