function solution(n) {
    const arr = [];
    n -= 1;
    arr.push((n % 3));
    let temp = 3;
    while (true) {
        if (n < temp) {
            break;
        }
        let chris = parseInt((n - temp) / 3);
        arr.push(chris);
        temp += temp * 3;
    }

    // 124로 만들고 합치기
    const answer = [];
    arr.forEach((n) => {
        let x = 0;
        switch (n) {
            case 0:
                x = 1;
                break;
            case 1:
                x = 2;
                break;
            case 2:
                x = 4;
                break;
        }
        answer.push(x);
    });
    answer.reverse();
    return answer.join('');
}

console.log(solution(2));