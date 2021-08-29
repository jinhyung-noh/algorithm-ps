import sys


def max_value():

    # inputs
    N, K = map(int, sys.stdin.readline().split())
    items = []  # [[weight1, value1], .. , [weightN, valueN]]
    for _ in range(N):
        weight, value = map(int, sys.stdin.readline().split())
        items.append([weight, value])


    table = [0] * (K + 1)   # table[i]: largest value of k weight

    for weight, value in items:
        for target in range(K, weight-1, -1):
            table[target] = max(table[target], table[target-weight] + value)

    print(table[-1])

max_value()
