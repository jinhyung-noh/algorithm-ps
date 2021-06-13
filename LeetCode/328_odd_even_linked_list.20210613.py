class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = odd_head  = ListNode(None)
        even = even_head  = ListNode(None)
        cur = head
        cnt = 1
        while cur:
            if cnt % 2 == 1:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
            cnt += 1

        odd.next = even_head.next 
        even.next = None

        return head


# solution in Book
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        # exception case
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
            # # more concise with "multi-assignment"
            # odd.next, even.next = odd.next.next, even.next, even.next.next
            # odd, even = odd.next, even.next

        # connect tail of odd to head of even
        odd.next = even_head
        return head