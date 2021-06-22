# separate chaining --> linked-list
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        import collections
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # insert and terminate if there is no Node of "index"
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return None
        
        # linked-list if there is Node of "index"
        p = self.table[index]
        while p:
            # already existing key --> update
            if p.key == key:
                p.value = value
                return None
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        # not existing index
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        # existing index
        while p:
            if p.key == key:
                return p.value
            else:
                p = p.next    
        # existing index but not existing key
        return -1 

    def remove(self, key: int) -> None:
        index = key % self.size
        # no index case
        if self.table[index].value is None:
            return None

        p = self.table[index]
        # first Node case
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return None
        while p.next:
            if p.next.key == key:
                p.next = p.next.next
                return None
            p = p.next
