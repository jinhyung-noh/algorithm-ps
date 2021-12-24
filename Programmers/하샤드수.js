function solution(x) {
    const digits = [];
    // 자리수 추출
    let temp = x;
    while (temp > 0) {
        digits.push(temp % 10);
        temp = parseInt(temp / 10);
    }
    console.log(digits);
    return;
}

solution(13);