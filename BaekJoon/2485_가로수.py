def 가로수():
    import sys
    input = sys.stdin.readline

    # 최대공약수 찾는 함수
    def gcd(a, b):
        # b가 0이 될때까지 반복
        while b:
            a, b = b, a % b
        return a

    N = int(input())
    # 간격들
    distances = []
    start = int(input())
    for i in range(N-1):
        end = int(input())
        distances.append(end - start)
        start = end

    # 간격들의 최대공약수를 찾고(모두 같은 간격이 되어야 하므로)
    gcd_dist = distances[0]
    for distance in distances[1:]:
        gcd_dist = min(gcd_dist, gcd(gcd_dist, distance))

    # 각 간격을 그 최대공약수 간격으로 만드는데 필요한 나무수를 계산
    cnt = 0
    for distance in distances:
        cnt += distance // gcd_dist - 1

    print(cnt)

가로수()