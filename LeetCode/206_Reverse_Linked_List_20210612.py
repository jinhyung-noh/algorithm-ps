class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev


# using recursion
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case
        if not head or not head.next:
            return head

        # recursion part
        result = self.reverseList(head.next)
        cur = result
        while cur.next:
            cur = cur.next
        cur.next = ListNode(head.val)
        return result
        

# solution in Book
# using recursion
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)
        

# using iteration
class Solution4:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev