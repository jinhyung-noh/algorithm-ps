function solution(new_id) {
    let temp = '';
    // 1: 소문자로 치환
    temp = new_id.toLowerCase();
    // 2: 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 제외 모든 문자 제거
    const answer = []
    for (let i = 0; i < temp.length; i++) {
        let ascii = temp[i].charCodeAt(0);
        console.log(ascii);
        if ((97 <= ascii && ascii <= 122) ||
            ascii == 77 || ascii == 78 || ascii == 95) {
            answer.push(temp[i]);
        }
    }
    console.log(answer);


    return answer;
}

new_id = '"...!@BaT#*..y.abcdefghijklm"';
solution(new_id);
