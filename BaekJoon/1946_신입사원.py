import sys


def 신입사원():

    # inputs
    num_cases = int(sys.stdin.readline())
    test_cases = [[] for _ in range(num_cases)]
    result = [0] * num_cases
    for i in range(num_cases):
        num_candidates = int(sys.stdin.readline())
        for _ in range(num_candidates):
            test_cases[i].append(tuple(map(int, sys.stdin.readline().split())))

        # sort
        test_cases[i].sort(key=lambda x: x[0])

       
        cnt = 0  # 탈락자
        temp_min = num_candidates
        # 첫번째 시험 1등부터 순차적으로 탐색하면서
        # 그때까지의 두번째 시험의 최고 성적을 기록한다
        for j in range(num_candidates):
            # 두번째 시험 기록 갱신
            # 다음 올 사람들은 첫번째 시험 기록이 안좋으므로
            # 이 기록보다 낮아야 채용 가능
            if test_cases[i][j][1] <= temp_min:
                temp_min = test_cases[i][j][1]
            # 첫번째 기록이 이전 사람들보다 안좋은 상태에서
            # 두번째 기록의 최고 성적보다 안좋으면 
            # 둘 다 자신보다 성적 좋은 사람이 있다
            else:
                cnt += 1

        result[i] = num_candidates - cnt

    print(*result, sep="\n")


신입사원()

