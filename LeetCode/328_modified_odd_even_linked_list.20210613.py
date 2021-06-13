class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = odd_head  = ListNode(None)
        even = even_head  = ListNode(None)
        cur = head
        while cur:
            # odd case
            if cur.val % 2 == 1:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next

        # 
        if head.val % 2 == 1:
            odd.next = even_head.next 
            even.next = None
        else:
            even.next = odd_head.next
            odd.next = None
        return head


def list2nodes(nums: list[int]) -> ListNode:
    head = cur = ListNode()         # 
    for num in nums:
        cur.val, cur.next = num, ListNode()
        cur = cur.next
    return head

def print_nodes(node: ListNode) -> None:
    head = node
    while head:
        print(head.val, end=" ")
        head = head.next
    print("")
    return None

nums = [1,2,3,4,5]
node_nums = list2nodes(nums)
print_nodes(Solution().oddEvenList(node_nums))