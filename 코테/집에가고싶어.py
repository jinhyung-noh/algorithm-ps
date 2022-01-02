
def home_plz():
    import sys
    input = sys.stdin.readline
    
    # inputs
    N, B = map(int, input().split())
    people = [0] * N
    for i in range(N):
        people[i] = list(map(int, input().split()))
    ###########################################

    # 업무종료시점 기준으로 정렬
    people.sort(key=lambda x: x[0])
    time = 0
    # 비는 시간이 최대한 없도록 앞사람부터 시작
    for person in people:
        # 아직 퇴근시간이 안되었으면 기다림
        if time < person[0]:
            time = person[0]
        
        # 해당 사람 드론 날림
        time += person[1] + B
    
    return print(time)

home_plz()
