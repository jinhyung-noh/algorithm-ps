function solution(n, computers) {
    // 이미 computers가 인접행렬
    let cnt = 0;
    const visited = Array.from({ length: n }, () => {
        return false;
    });

    function _dfs(curr) {
        // 현재 노드 방문처리
        visited[curr] = true;

        // 인접한 노드 탐색(방문하지 않았고, 자기 자신이 아닌)
        for (let i = 0; i < n; i++) {
            if (computers[curr][i] == 1) {
                // i: next node
                if (i !== curr && !visited[i]) {
                    _dfs(i);
                }
            }
        }
    }

    // 처음부터 탐색 시작
    for (let com = 0; com < n; com++) {
        // 방문하지 않았으면 네트워크수 올리고, dfs 탐색 시작
        if (!visited[com]) {
            cnt++;
            _dfs(com);
        }
    }

    return cnt;
}

const n = 3;
const computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]];
console.log(solution(n, computers));