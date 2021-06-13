class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
    
stack = Stack()
for i in range(1, 5+1):
    stack.push(i)

for _ in range(5):
    print(stack.pop())
