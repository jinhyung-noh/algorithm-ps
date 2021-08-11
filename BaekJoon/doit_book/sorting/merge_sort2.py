
def merge_sort(arr: list):

    def _merge(start, middle, end):
        """merge two sorted array"""
        
        i = k = start
        j = middle + 1

        # 둘 중 작은것부터 buff 채움
        while i <= middle and j <= end:
            if arr[i] <= arr[j]:
                buff[k] = arr[i]
                i += 1
            else:
                buff[k] = arr[j]
                j += 1
            k += 1

        # left side 남은 것 처리
        while i <= middle:
            buff[k] = arr[i]
            i += 1
            k += 1
        # right side 남은 것 처리
        while j <= end:
            buff[k] = arr[j]
            j += 1
            k += 1

        # copy buff to original arr
        for i in range(start, end+1):
            arr[i] = buff[i]

    def _merge_sort(start, end):
        # 원소의 개수 1보다 클때만

        if start < end:
            middle = (start + end) // 2

            _merge_sort(start, middle)
            _merge_sort(middle+1, end)
            _merge(start, middle, end)

    n = len(arr)
    buff = [0] * n
    _merge_sort(0, n-1)
        

arr = list(range(9, -1, -1))
print(arr)
merge_sort(arr)
print(arr)
