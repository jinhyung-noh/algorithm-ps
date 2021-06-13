class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# conver ListNode to list
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        word = []
        while head:
            word.append(head.val)
            head = head.next
        
        return word == word[::-1]


# solution in Book
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        q: list = []

        if not head:
            return True

        node = head
        # convert to list
        while node is not None:
            q.append(node.val)
            node = node.next

        # determine palindrome
        # pop(0) is O(n) in list --> not effective!
        while len(q) > 1:
            if q.pop() != q.pop(0):
                return False
        return True


# using Deque in collections module
class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        from collections import deque
        q: deque = deque()

        if not head:
            return True

        node = head
        while node is not None:
            if q.popleft() != q.pop():
                return False
        return True

# using "Runner" solution
class Solution4:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # in odd-case : move slow next
        # e.g. head / slow / rev : 1-2-3-2-1 / 1-2-3 / 2-1
        if fast:
            slow = slow.next

        while slow:
            if slow.val != rev.val:
                return False
            else:
                slow, rev = slow.next, rev.next
        return False