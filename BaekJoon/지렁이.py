R = [[3,9,2,7],[10,6,8,4],[1,4,9,10],[5,7,8,4]]	

# [[3, 9, 2, 7]
#  [10, 6, 8, 4]
#  [1, 4, 9, 10]
#  [5, 7, 8, 4]]

def solution(R):
    W = len(R[0])
    H = len(R)
    visited = [[False]*H for _ in range(W)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = [0] # 최댓값

    def dfs(x, y, length):

        cnt = 4   # 4방향 모두 포문 돌았을때 4가 살아있다면 --> 막힌 것
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # new_x, new_y가 유효한 범위내 있고, 그 위치값이 이전 x,y 좌표 값보ㅗ다 크고 미방문 상태면 
            # 거기로 dfs 순회 또하는거징
            if 0 <= new_x < H and 0 <= new_y < W and R[new_x][new_y] > R[x][y] and not visited[new_x][new_y]:
                    cnt -= 1;
                    visited[new_x][new_y] = True
                    dfs(new_x, new_y, length + 1)
                    visited[new_x][new_y] = False 
        
        # 탐색이 완료되면 뱀의 길이를 확인해서 최댓값이랑 비료를 하려고 하는 것
        if cnt == 4:    # 4가 남아있다는 것은 더 갈데가 없는 점 --> 마지막점
            # cnt==4라는것은 마지막 지점 --> 뱀의 길이를 비교해야됨
            answer[0] = max(answer[0], length)


    # 모든 시작점에서 지렁이 start
    for x in range(H):
        for y in range(W):
            visited[x][y] = True
            dfs(x, y, 1)
            visited[x][y] = False

    return answer[0]

print(solution(R))