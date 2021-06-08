# recursion쓸때는 Helper function 쓴다 ; 뒤에 넘겨주는 상수같은거 처리할 때 (초기값을 정할 수 있으므로)
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Recursive Version
class Solution1:
    def addTwoNumbers(self, l1, l2):
        return Solution1().addTwoNumbersHelper(l1, l2, 0)  # Helperfucntion for recursive initiation ;
    def addTwoNumbersHelper(self, l1, l2, c):              # 단계마다 넘기는 정보 초기화할때 사용
        if l1 == None and l2 == None:
            return None
        else:
            if l1 == None :
                l1 = Node(0)
            if l2 == None :
                l2 = Node(0)
            val = l1.val + l2.val + c
            c = val // 10
            result = Node(val % 10)
            result.next = Solution1().addTwoNumbersHelper(l1.next, l2.next, c)
            return result

# Iterative version
class Solution2:
    def addTwoNumbers(self, l1, l2):
        a = l1
        b = l2
        c = 0
        ret = current = None

        while a or b:
            val = a.val + b.val + c
            c = val // 10
            if not current:
                ret = current = Node(val % 10)  # ret를 처음에만 current라고 하면
            else:
                current.next = Node(val % 10)
                current = current.next          # 이 이후에는 ret는 첫 current를 지칭하고
            if a.next or b.next:                # current는 다른 값이 된다 : current.next.next. ... .next
                if not a.next:                  # 따라서 마지막에는 ret는 첫 Node, current는 마지막 Node가 된다
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            a = a.next
            b = b.next
        print(ret.val, current.val)
        return ret

# l1 = 3 - 4- 2
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
l1.next.next.next = Node(7)

# l2 = 4 - 6 - 5
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

# answer = Solution1().addTwoNumbers(l1, l2)
answer = Solution2().addTwoNumbers(l1, l2)
while answer:
    print( answer.val )
    answer = answer.next

