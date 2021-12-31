function solution(participant, completion) {
    // participant 오브젝트화 (해시 이용)
    const hash = {};
    for (let i = 0; i < participant.length; i++) {
        // 없으면 1로 초기화
        if (!hash[participant[i]]) {
            hash[participant[i]] = 1;
            continue;
        }
        // 있으면 ++
        hash[participant[i]]++;
    }
    // completion 순회하면서 hash에서 하나씩 빼기
    for (let i = 0; i < completion.length; i++) {
        hash[completion[i]]--;
    }
    // 남은 참가자 찾기
    for (let key in hash) {
        if (hash[key] == 1) {
            return key;
        }
    }
    return;
}

participant = ["mislav", "stanko", "mislav", "ana"];
completion = ["stanko", "ana", "mislav"];

console.log(solution(participant, completion));