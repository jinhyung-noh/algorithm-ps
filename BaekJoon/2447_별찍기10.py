import sys

N = int(sys.stdin.readline())
k = 0
while N > 3 ** k:
    k += 1
arr = [[0] * N for _ in range(N)]
# arr = [""] * N



def printing(k: int, x: int, y: int):
    def _trisect(k: int , x: int):
        if 0 <= x < 3 ** (k-1):
            return 0
        elif 3 ** (k-1) <= x < 2 * 3 ** (k-1):
            return 1
        else:
            return 2

    # def _printing(k: int, x: int, y: int):
    #     # base case 1
    #     if x == 0 and y == 0:
    #         return 1
    #     # base case 2
    #     if 3 * _trisect(k, x) + _trisect(k, y) == 4:
    #         return 0

    #     # recursive call
    #     return _printing(k-1, x % 3 ** (k-1), y % 3 **(k-1))

    # if _printing(k, x, y):
    #     return "*"
    # else:
    #     return " "

    while k > 0:
        if 3 * _trisect(k, x) + _trisect(k, y) == 4:
            return " "
        k -= 1
        x %= 3 ** k
        y %= 3 ** k
    return "*"
    



for i in range(N):
    for j in range(N):
        arr[i][j] = printing(k, i, j)
        # arr[i] += printing(k, i, j)

for i in range(N):
    print("".join(arr[i]))
    # print(arr[i])