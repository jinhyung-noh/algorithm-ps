class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def List2Nodes(nums: list) -> ListNode:
            # base case: nums == []
            if not nums:
                return None
            else:
                result = ListNode(nums[0])
                result.next = List2Nodes(nums[1:])
            return result
            
        result = []
        while l1 or l2:
            state = 0
            if l1 and l2:
                if l1.val <= l2.val:
                    state = 1
                else:
                    state =2
            elif l1:
                state = 1
            else:
                state = 2

            if state == 1:
                result.append(l1.val)
                l1 = l1.next
            else:
                result.append(l2.val)
                l2 = l2.next

        return List2Nodes(result)


# solution in Book
# using recursion
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l2

nums = [1,2,3]
node_nums = Solution().List2Nodes(nums)
print(Solution().Nodes2List(node_nums))