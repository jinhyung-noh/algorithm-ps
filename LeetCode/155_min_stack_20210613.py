class MinStack:
    import sys
    def __init__(self):
        self.head = None
    def push(self, val: int) -> None:
        self.head = Node(val, self.head)
    def pop(self) -> None:
        self.head = self.head.next
    def top(self) -> int:
        return self.head.val
    def getMin(self) -> int:
        result = sys.maxsize
        cur = self.head
        while cur:
            result = min(result, cur.val)
            cur = cur.next
        return result
class Node:
    def __init__(self, val=None, next=None):
        self.val = val 
        self.next = next