from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """merge sort a[left]..a[right]"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center+1, right)

            p = j = 0
            i = k = left

            # copy head to buffer
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            # compare buffer and tail -> merge
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
                
            # merge remaining buffer
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1


    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n-1)
    del buff

print("\n\n=========  merge sort ========\n\n")
num = int(input('Enter an integer(number of elements): '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
merge_sort(x)

print('오름차순으로 정렬했습니다...')
print(x)

            