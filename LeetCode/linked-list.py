class ListNode: def __init__(self, val=None, next=None): self.val = val
        self.next = next

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
print_nodes(node_nums)

        