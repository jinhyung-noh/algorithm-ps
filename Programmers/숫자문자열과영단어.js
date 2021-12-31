function solution(s) {
    const digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

    let answer = [];
    for (let i = 0; i < s.length; i++) {
        // 숫자인 경우
        if (digits.indexOf(s[i]) >= 0) { // digits에서 
            answer.push(s[i]);
            continue;
        }
        // 문자인 경우
        let temp;
        switch (s[i]) {
            case 'z': // 0
                temp = '0';
                i += 3;
                break;
            case 'o': // 1
                temp = '1';
                i += 2;
                break;
            case 't':
                if (s[i + 1] == 'w') { // 2
                    temp = '2';
                    i += 2;
                }
                else {   // 3
                    temp = '3';
                    i += 4;
                }
                break;
            case 'f':
                if (s[i + 1] == 'o') { // 4
                    temp = '4';
                    i += 3;
                }
                else {  // 5
                    temp = '5';
                    i += 3;
                }
                break;
            case 's':
                if (s[i + 1] == 'i') { // 6
                    temp = '6';
                    i += 2;
                }
                else {
                    temp = '7';
                    i += 4;
                }
                break;
            case 'e':
                temp = '8';
                i += 4;
                break;
            case 'n':
                temp = '9';
                i += 3;
                break;
        }
        answer.push(temp);
    }
    // 문자열로 변환
    answer = answer.join('');

    // number로 변환
    answer = parseInt(answer);
    return answer;
}

s = "000";
console.log(solution(s));