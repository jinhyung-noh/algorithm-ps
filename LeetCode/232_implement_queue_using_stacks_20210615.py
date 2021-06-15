class MyQueue:
    def __init__(self):
        # stack operation
        # pop  : list.pop()
        # push : list.append() 
        self.main_stack = []
        self.sub_stack = []

    def push(self, x: int) -> None:
        # move all element in main_stack to sub_stack
        while self.main_stack:
            self.sub_stack.append(self.main_stack.pop())
        # push new element to main_stack
        self.main_stack.append(x)
        # re-move all element in sub_stack to main_stack
        while self.sub_stack:
            self.main_stack.append(self.sub_stack.pop())

    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return len(self.main_stack) == 0


# solution in Book
class MyQueue2:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # if there is not output --> put all elements again
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []