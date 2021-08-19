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
                return '1'
            return '0'

        # recursive call
        result = ''
        for i in range(4):
            quadrants[k-1] = i
            result += _recur(k-1)

        # merge into bigger part to level k+1
        if result == '1111':     # blue merge
            return '1'
        if result == '0000':   # white merge
            return '0'
        return '(' + result + ')'

    # inputs
    N = int(sys.stdin.readline())
    arr = [None] * N
    for i in range(N):
        arr[i] = list(sys.stdin.readline().strip())

    temp = N
    k = -1
    while temp:
        k += 1
        temp //= 2
    quadrants = [None] * k


    print(_recur(k))
    return


colored_paper()