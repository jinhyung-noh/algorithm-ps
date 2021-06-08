# my solution
class Node():
    def __init__(self, num=None):
        self.num = num
        self.next = None


class Solution():
    # show all the nodes in order
    def showAllNodes(self, node):
        while node:
            print(node.num)
            node = node.next
    # recursive로 해봄
    def showAllNodesRec(self, node):
        if node == None:
            return None
        print(node.num)
        return self.showAllNodesRec(node.next)

    # list --> linked list
    def list2LL(self, ls):
        if ls ==[]:
            return None
        else:
            result = Node(ls[0])
            result.next = Solution().list2LL(ls[1:])
            return result
    # LL --> list
    def LL2list(self, node):
        if node == None:
            return []
        else:
            result = [node.num]
            result += self.LL2list(node.next)
            return result

    # list를 만들고 거꾸로 list 생성 : time O(2n), space O(n)
    def reverseLL1(self, node):
        # LinkedList --> list
        num_list = self.LL2list(node)
        # reversed list --> LinkedList
        result = self.list2LL(num_list[::-1])
        return result

    # iteration / using pointer : time O(n), space O(1)
    def reverseLL2(self, node):
        prev = None
        while node:
            if prev == None:
                prev = Node(node.num)
                node = node.next
            else:
                temp = Node(node.num)
                temp.next = prev
                prev = temp
                node = node.next
        return prev

# a = Node(1)
# a.next = Node(2)
# a.next.next = Node(3)
# a.next.next.next = Node(4)
# a.next.next.next.next = Node(5)
# # num_list = [1, 2, 3, 4, 5]
# # b = Solution().list2LL(num_list)
#
# answer = Solution().reverseLL3(a)
#
# Solution().showAllNodes(answer)

#################################################
# sol by TechLead
class Node2(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res


class Solution2(object):
    def reverse(self, node):
        curr = node
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

node = Node2(1, Node2(2, Node2(3, Node2(4, Node2(5)))))

print(Solution2().reverse(node))