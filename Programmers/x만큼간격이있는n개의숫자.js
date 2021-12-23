function solution(x, n) {
    var answer = [];
    let i = 1;
    while (answer.length < n) {
        answer.push(x * i);
        i++;
    }
    return answer;
}