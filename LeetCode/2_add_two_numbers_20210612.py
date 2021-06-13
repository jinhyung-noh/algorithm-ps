class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add_rec(l1: ListNode, l2: ListNode, remainder: int) -> ListNode:
            # base case : both l1, l2 is None
            if not l1 and not l2:
                if remainder:
                    return ListNode(remainder)
                else:
                    return None
            # semi base case : one of l1, l2 is None 
            # -> assume the other Node(0)
            if not l1:
                return add_rec(ListNode(), l2, remainder)
            elif not l2:
                return add_rec(l1, ListNode(), remainder)

            # recursion
            addition = l1.val + l2.val + remainder
            result = ListNode(addition % 10)
            remainder = addition // 10
            result.next = add_rec(l1.next, l2.next, remainder)
            return result

        return add_rec(l1, l2, 0)


# solution in Book
# convert into list --> add --> re-convert into Linked-list
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = int(''.join(self.toList(l1)[::-1]))
        num2 = int(''.join(self.toList(l2)[::-1]))
        two_sum = num1 + num2
        return self.toReversedLinkedList([int(char) for char in str(two_sum)])

    # convert linked-list to list
    def toList(self, l1: ListNode) -> list[str]:
        result = []
        while l1:
            result.append(str(l1.val))
            l1 = l1.next
        return result

    # convert list to reversed-linked-list:
    def toReversedLinkedList(self, digits: list) -> ListNode:
        prev: ListNode = None
        for digit in digits:
            node = ListNode(digit)
            node.next = prev
            prev = node

        return node


# another solution
class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # sum of two inputs
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            # quotient and remainder
            carry, remainder = divmod(sum+carry, 10)
            head.next = ListNode(remainder)
            head = head.next
        return root.next