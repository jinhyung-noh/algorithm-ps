class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# using hash
class Solution:
    def _mergeKListsHelper(self, lists: list[ListNode]) -> list:
        from collections import defaultdict

        hash = defaultdict(lambda: 0)
        for sub_list in lists:
            while sub_list:
                hash[sub_list.val] += 1
                sub_list = sub_list.next
            
        sorted_keys = sorted(hash.keys())
        result = []
        for key in sorted_keys:
            result += [key] * hash[key]
        return result

    def mergeKLists(self, lists):
        result = head =  ListNode(None)
        for num in self._mergeKListsHelper(lists):
            result.next = ListNode(num)
            result = result.next
        return head.next


# solution in Book
class Solution2:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        import heapq
        root = result = ListNode(None)
        heap = []

        # store the root of each linked-list
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # pop heap --> store next node
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next