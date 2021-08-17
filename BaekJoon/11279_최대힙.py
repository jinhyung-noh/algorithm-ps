import sys

def max_heap():

    def heapify():

        N = len(heap)
        parent = 0

        while parent <= ((N-1)-1)//2:   # last parent
            # choose bigger child
            child = 2 * parent + 1
            if child <= N - 2 and heap[child+1] > heap[child]:
                child += 1
            
            # compare and swap
            if heap[child] > heap[parent]:
                heap[parent], heap[child] = heap[child], heap[parent]
            parent = child

    def heappush(x: int):
        heap.append(x)
        N = len(heap)
        child = N - 1
        while child > 0:
            parent = (child - 1) // 2
            # compare and swap
            if heap[child] > heap[parent]:
                heap[child], heap[parent] = heap[parent], heap[child]
            child = parent

    def heap_operation(order: int):
        if order == 0:
            if len(heap) == 0:
                answers.append(0)
                return

            # swap heap[0], heap[-1]
            heap[0], heap[-1] = heap[-1], heap[0]
            answers.append(heap.pop())
            heapify()
            return
        
        else:
            heappush(order)


    heap = []
    answers = []

    # inputs
    n = int(sys.stdin.readline())
    for _ in range(n):
        order = int(sys.stdin.readline())
        heap_operation(order)

    # outputs
    for answer in answers:
        print(answer)

max_heap()