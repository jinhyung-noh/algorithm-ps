import sys

n = int(sys.stdin.readline())
words = set() 
for i in range(n):
    words.add(sys.stdin.readline().strip())

# using merge sort
def merge_sort(arr: list):
    
    def _merge(start, middle, end):

        i = k = start
        j = middle + 1

        while i <= middle and j <= end:
            if len(arr[i]) < len(arr[j]):
                buff[k] = arr[i]
                i += 1
            elif len(arr[i]) > len(arr[j]):
                buff[k] = arr[j]
                j += 1
            # 같은 경우 2차 조건 대입
            else:
                if arr[i] < arr[j]:
                    buff[k] = arr[i]
                    i += 1
                else:
                    buff[k] = arr[j]
                    j += 1
            k += 1

        # left side 
        while i <= middle:
            buff[k] = arr[i]
            i += 1
            k += 1
        # right side
        while j <= end:
            buff[k] = arr[j]
            j += 1
            k += 1
        # copy buff to original arr
        for i in range(start, end+1):
            arr[i] = buff[i]
            
    def _merge_sort(start, end):
        if start < end:
            middle = (start + end) // 2

            _merge_sort(start, middle)
            _merge_sort(middle+1, end)
            _merge(start, middle, end)
    
    n = len(arr)
    buff = [0] * n
    _merge_sort(0, n-1)

words = list(words)
merge_sort(words)

for word in words:
    print(word) 