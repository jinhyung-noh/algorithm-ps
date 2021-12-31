function solution(tickets) {
    // 인접리스트 구성
    const graph = {};
    for (let i = 0; i < tickets.length; i++) {
        if (graph[tickets[i][0]]) {
            graph[tickets[i][0]].push(tickets[i][1]);
            continue;
        }
        graph[tickets[i][0]] = [tickets[i][1]];
    }

    // 인접리스트 정렬: 내림차순
    for (let key in graph) {
        graph[key] = graph[key].sort((a, b) => {
            if (a < b) return 1;
            if (a > b) return -1;
            if (a === b) return 0;
        });
    }
    console.log(graph);
    const answer = [];
    function dfs(curr) {
        return;
    }
    return;
}


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]];
solution(tickets);