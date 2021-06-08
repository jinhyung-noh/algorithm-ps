# stack 자료구조
# sol by TechLead

class MaxStack(object):
    """
    Consists of two stacks : org stack, max stack

    self.stack  (e.g., 1,2,3,2)
    self.maxes  last value is the max value of stack (e.g., 1,2,3,3)
    """
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):
        self.stack.append(val)
        if self.maxes and self.maxes[-1] > val:
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
# for i in range(4):
#     print('max', s.max())
#     print(s.pop())

s1 = MaxStack()
s3 = s1
s2 = MaxStack()
print(s1 == s3)