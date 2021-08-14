import sys

def colored_paper():
    
    def get_x():
        x = 0
        for i in range(k-1, -1, -1):
            x += (quadrants[i] // 2) * 2 ** i
        return x

    def get_y():
        y = 0
        for i in range(k-1, -1, -1):
            y += (quadrants[i] % 2) * 2 ** i
        return y

    def _recur(k: int):

        # base case: level 0
        if k == 0:
            x = get_x()
            y = get_y()
            val = arr[x][y]
            # blue or white
            if val:
                cnt[0] += 1
                return 1, 0
            else:
                cnt[1] += 1
                return 0, 1

        # recursive call
        blues = 0
        whites = 0
        for i in range(4):
            quadrants[k-1] = i
            blue, white = _recur(k-1)
            blues += blue
            whites += white

        # merge into bigger part to level k+1
        if blues == 4:     # blue merge
            cnt[0] -= 3
            return 1, 0
        if whites == 4:   # white merge
            cnt[1] -= 3
            return 0, 1
        return 0, 0

    # inputs
    N = int(sys.stdin.readline())
    arr = [None] * N
    for i in range(N):
        arr[i] = list(map(int, sys.stdin.readline().split()))

    temp = N
    k = -1
    while temp:
        k += 1
        temp //= 2
    quadrants = [None] * k


    cnt = [0, 0] # blue and white
    _recur(k)
    print(cnt[1])
    print(cnt[0])
    return


colored_paper()