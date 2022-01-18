def 강의실배정():
    import sys
    import heapq

    N = int(sys.stdin.readline())
    lectures = []
    for i in range(N):
        start, end = map(int, sys.stdin.readline().split())
        # 먼저 시작하는 강의 순서 --> 우선순위큐
        heapq.heappush(lectures, (start, end))

    # lecture_rooms: 각 강의실의 마지막 강의 시간 기록
    # 가장 먼저 끝나는 강의실 구분 위해 heapq 사용
    lecture_rooms = [heapq.heappop(lectures)[1]] # 일단 하나 먼저 넣기
    while lectures:
        start, end = heapq.heappop(lectures)
        # 가장 먼저 끝나는 강의실보다 전에 시작하면 새 강의실 배정
        if start < lecture_rooms[0]:
            heapq.heappush(lecture_rooms, end)
            continue
        # 아닐 경우 그 강의실에 강의 배정(끝나는 시간 갱신)
        heapq.heappop(lecture_rooms)
        heapq.heappush(lecture_rooms, end)

    print(len(lecture_rooms))
        
강의실배정() 