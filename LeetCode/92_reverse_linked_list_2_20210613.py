class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        root = start = ListNode(None)
        root.next = head

        # start, end
        for i in range(left-1):
            start = start.next
        end = start.next

        # reverse m to n
        for i in range(left, right):
            temp = end.next.next
            end.next.next = start.next
            start.next = end.next
            end.next = temp
        
        return root.next


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
print_nodes(Solution().reverseBetween(node_nums, 2,4))
