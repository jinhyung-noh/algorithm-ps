# using heap_sort
import sys

def heapify(arr: list, left: int, right: int):
    parent = left

    while parent <= (right-1)// 2:  # while parent is "parent node"
        # choose bigger child
        child = 2 * parent + 1
        if child + 1 <= right and arr[child] < arr[child+1]:
            child += 1

        # swap if child node is bigger than parent node
        if arr[parent] >= arr[child]:
            break
        else:
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child


n = int(sys.stdin.readline())
heap = [0] * n

for i in range(n):
    heap[i] = int(sys.stdin.readline())


# heapify all elemensts of heap
for i in range((n-1)//2, -1, -1):
    heapify(heap, i, n-1)

for i in range(n-1, 0, -1):
    # swap
    heap[0], heap[i] = heap[i], heap[0]
    heapify(heap, 0, i-1)

for num in heap:
    print(num)







