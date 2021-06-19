class MyCircularQueue:
    def __init__(self, k: int):
        self.length = k
        self.array = [None] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        # full
        if self.isFull():
            return False
        # empty case
        elif self.isEmpty():
            self.array[self.rear] = value
            return True
        # normal case
        else:
            self.rear = (self.rear + 1) % self.length
            self.array[self.rear] = value
            return True

    def deQueue(self) -> bool:
        # empty 
        if self.isEmpty():
            return False

        self.array[self.front] = None
        # more than one element
        if self.front != self.rear:
            self.front = (self.front + 1) % self.length
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.rear]
    
    def isEmpty(self) -> bool:
        return (self.front == self.rear) and (self.array[self.front] == None)
        
    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.length and self.array[self.rear] != None


# solution in Book
class myCircularQueue2:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

   # enQueue(): move rear pointer
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
           self.q[self.p2] = value
           self.p2 = (self.p2 + 1) % self.maxlen
           return True
        else:
            return False 

    # deQeueu(): move front pointer
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2] is None else self.q[self.p2]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p2] is not None

        
