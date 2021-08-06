import sys

N = int(sys.stdin.readline())

def hansu(N):
    # 1 or 2 digits
    if 1 <= N < 100:
        return N

    # 3 digits
    cnt = 0
    exceeded = False

    for i in range(1, 10):
        if exceeded:
            break

        for j in range(0, 10):
            k = 2 * j - i       # 마지막 자리수
            if 0 <= k <= 9:
                if 100*i + 10*j + k <= N:
                    cnt += 1
                else:
                    exceeded = True
                    break
    return 99 + cnt

print(hansu(N))




