class Sort():
    def bubble_sort(self, arr: list):
        n = len(arr)

        for i in range(n, 1, -1):
            for j in range(1, i):
                # swap
                if arr[j-1] > arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    

    def selection_sort(self, arr: list):
        n = len(arr)

        for i in range(n-1):
            # find minimum idx: i .. n-1
            min_idx = i
            for j in range(i, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            # swap
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def insertion_sort(self, arr: list):
        n = len(arr)

        for i in range(1, n):
            while i-1 >= 0 and arr[i-1] > arr[i]:
                # swap 
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i -= 1

    def quick_sort(self, arr: list):

        def _quick_sort_helper(start, end):
            """using arr[start] as a pivot"""

            # base case
            if start >= end:
                return

            # take pivot midlle of array
            mid = (start + end) // 2
            arr[mid], arr[start] = arr[start], arr[mid]
            
            left = pivot = start
            right = end

            while left < right:
                # move pointers
                while left < end and arr[left] <= arr[pivot]: left += 1
                while arr[right] > arr[pivot]: right -= 1

                # check and swap
                if left >= right:        # final state: equal or crossed
                    arr[pivot], arr[right] = arr[right], arr[pivot]
                else:                   # normal state
                    arr[left], arr[right] = arr[right], arr[left]

            # recursive call: sort left part and right part
            _quick_sort_helper(start, right)
            _quick_sort_helper(left, end)

        _quick_sort_helper(0, len(arr)-1)


    def merge_sort(self, arr: list):

        def _merge(start: int, end: int):
            """merge two groups: arr[start: mid+1] and arr[mid: end+1] in smaller order"""
            mid = (start + end) // 2
            i = k = start
            j = mid + 1

            # merge in small order
            while i <= mid and j <= end:
                if arr[i] < arr[j]:
                    buff[k] = arr[i]
                    i += 1
                else:
                    buff[k] = arr[j]
                    j += 1
                k += 1
            
            # move remaining part
            while i <= mid:
                buff[k] = arr[i]
                i += 1
                k += 1
            while j <= end:
                buff[k] = arr[j]
                j += 1
                k += 1
            
            # copy buff to arr
            for i in range(start, end+1):
                arr[i] = buff[i]

        def _merge_sort_helper(start: int, end: int):
            # base case: less or equal than 1 element
            if start >= end:
                return

            # recursive call
            # divide into two parts --> merge
            mid = (start + end) // 2
            _merge_sort_helper(start, mid)
            _merge_sort_helper(mid+1, end)

            _merge(start, end)

        n = len(arr)
        buff = [0] * n
        _merge_sort_helper(0, n-1)

    def heap_sort(self, arr: list):

        def _heapify(start, end):
            """heapify undef the `node`"""
            parent = start
            while parent <= (end - 1) // 2:  # start is parent node
                # choose bigger child node
                child = 2 * parent + 1
                if child + 1 <= end and arr[child] < arr[child+1]:
                    child += 1
                
                # compare arr[parent] and arr[child] --> swap
                if arr[parent] < arr[child]:
                    arr[parent], arr[child] = arr[child], arr[parent]
                    parent = child
                else:
                    break

        n = len(arr)

        # heapify all arr: heapify from last parent to first parent
        for parent in range((n-1)//2, -1, -1):
            _heapify(parent, n-1)

        # sort using heap
        for i in range(n-1, 0, -1): 
            arr[0], arr[i] = arr[i], arr[0]
            _heapify(0, i-1)




arr = list(range(9, -1, -1))
print("========= original arr =========")
print(arr)
# Sort().bubble_sort(arr)
# Sort().selection_sort(arr)
# Sort().insertion_sort(arr)
# Sort().quick_sort(arr)
# Sort().merge_sort(arr)
# Sort().heap_sort(arr)
print("========= sorted arr =========")
print(arr)