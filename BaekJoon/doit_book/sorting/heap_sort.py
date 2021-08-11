from typing import MutableSequence


def heap_sort(a: MutableSequence) -> None:
    """heap sort"""

    def heapify(a: MutableSequence, left: int, right: int) -> None:
        """heapify parent node a[left]"""

        parent = left
        while parent <= (right - 1) // 2:   # lask parent node: (right-1)//2
            child = 2 * parent + 1
            if child <= right - 1 and a[child] < a[child+1]:    
                child = child + 1        # 자식 노드 중 더 큰 값
            
            # 자식노드보다 크거나 같으면 break
            if a[parent] >= a[child]:
                break

            # swapping
            a[parent], a[child] = a[child], a[parent]
            parent = child
        
    n = len(a)
    # first heapify all array
    # 가장 낮은 parent node인 (n-1)//2 부터 시작(역순)
    for i in range((n-1)//2, -1, -1):
        heapify(a, i, n-1)

    # swap a[0] and a[i] (because a[0] is max of 0..i)
    # then re-heapify 0..(i-1) // (i..n-1) is already sorted
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]      # swap last of unsorted part(a[0..i])
        heapify(a, 0, i-1)


# a = list(range(10,-1,-1))
# import random
# a = [random.randint(1, 20) for i in range(20)]
# heap_sort(a)
# print(a)


##############################
# heapq 모듈 이용하는 방법

import heapq
from typing import MutableSequence

def heap_sort2(a: MutableSequence) -> None:
    """heap sort using heapq.push and heapq.pop"""

    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop()