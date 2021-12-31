function solution(answers) {
    const supo_1 = [1, 2, 3, 4, 5];                // 5단위 반복
    const supo_2 = [2, 1, 2, 3, 2, 4, 2, 5];       // 8단위 반복
    const supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; // 10단위 반복
    const ans_cnt = [0, 0, 0]; // answ_cnt[i-1]: i번째 수포자의 정답 개수

    // answer 순회하면서 정답 체크
    for (let i = 0; i < answers.length; i++) {
        let answer = answers[i];
        // 1번수포자
        if (answer === supo_1[i % 5]) {
            ans_cnt[0] += 1;
        }
        // 2번수포자
        if (answer === supo_2[i % 8]) {
            ans_cnt[1] += 1;
        }
        // 3번수포자
        if (answer === supo_3[i % 10]) {
            ans_cnt[2] += 1;
        }
    }

    const answer = [];
    let maxi = Math.max(...ans_cnt);
    for (let i = 0; i < 3; i++) {
        if (ans_cnt[i] === maxi) {
            answer.push(i + 1);
        }
    }
    return answer;
}
answers = [1, 2, 3, 4, 5];
console.log(solution(answers));