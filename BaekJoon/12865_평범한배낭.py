import sys


def max_value():

    # inputs
    N, K = map(int, sys.stdin.readline().split())
    items = []  # [[weight1, value1], .. , [weightN, valueN]]
    for _ in range(N):
        weight, value = map(int, sys.stdin.readline().split())
        items.append([weight, value])


    table = [0] * (K + 1)   # table[i]: largest value of k weight

    # 각 물건마다 고려한다
    for weight, value in items:
        # 각 무게마다 물건의 무게를 뺀 만큼의 가치에서 물건의 가치를 더한 것과 비교
        # 물건을 하나만 쓸 수 있으므로 역순으로 비교
        for target in range(K, weight-1, -1):
            table[target] = max(table[target], table[target-weight] + value)

    print(table[-1])

max_value()
