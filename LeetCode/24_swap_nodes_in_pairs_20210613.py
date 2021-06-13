class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case 
        if not head or not head.next:
            return head

        # recursion
        result = ListNode(head.next.val, head)
        result.next.next = self.swapPairs(head.next.next)
        return result


# solution in Book
# just swap val; not node itself
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # swap values
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

class Solution3:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # let b to point a(head)
            b = head.next
            head.next = b.next
            b.next = head

            # let prev to pint b
            prev.next = b

            # move 2 times
            head = head.next
            prev = prev.next.next

        return root.next


# using recursion
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # return swapped value
            head.next = self.swapPairs(p,next)
            p.next = head
            return p
        return head
