def solution(board, moves):
    import sys

    N = len(board)
    # 가로, 세로를 바꾸자 (밑에서부터 차곡차곡)
    new_board = [[] for i in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(N):
            if board[i][j] != 0:
                new_board[j].append(board[i][j])

    # moves대로 인형뽑고 빈 스택에 쌓기
    stack = [] # 인형 쌓는 공간
    cnt = 0    # 같은 인형 만나면 터뜨린 횟수
    for move in moves:
        move -= 1   # index처리(1,2,3,4,5 -> 0,1,2,3,4)

        try:
            curr_doll = new_board[move].pop()   # new_board의 move 열에서 새 인형 뽑는다
        except:
            curr_doll = False                   # 빈 리스트일경우 예외처리

            
        if stack and stack[-1] == curr_doll:    # 뽑은 인형이 stack[-1]과 같을때 터뜨린다
            stack.pop()
            cnt += 2    # 한번 터뜨릴때마다 인형 2개씩 터지네 ㅠㅠ
            continue
        elif curr_doll: # curr_doll 있을때는 stack에 넣어준다
            stack.append(curr_doll)

    return cnt
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board, moves)



