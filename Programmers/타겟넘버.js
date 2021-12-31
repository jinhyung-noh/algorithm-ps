// // dfs
// function solution(numbers, target) {
//     const N = numbers.length;
//     let cnt = 0;

//     // dfs
//     function _dfs(idx, total, sign) {
//         total += sign * numbers[idx];
//         // base case
//         if (idx === N - 1) {
//             if (total === target) {
//                 cnt += 1;
//             }
//             return;
//         }
//         for (let sign = 1; sign >= -1; sign -= 2) {
//             _dfs(idx + 1, total, sign);
//         }
//     }
//     _dfs(0, 0, +1);
//     _dfs(0, 0, -1);
//     return cnt;
// }

// bfs
function solution(numbers, target) {

    const q = [[0, 0, +1], [0, 0, -1]]; // (idx, total, sign)
    let cnt = 0;

    while (q.length > 0) {
        let [curr_idx, curr_total, curr_sign] = q.shift();
        curr_total += curr_sign * numbers[curr_idx];

        // 탈출조건
        if (curr_idx === numbers.length - 1) {
            // 원하는 케이스
            if (curr_total === target) {
                cnt += 1;
            }
            continue;
        }

        // 아닐경우 계속 bfs 탐색
        if (curr_idx < numbers.length - 1) {
            q.push([curr_idx + 1, curr_total, +1]);
            q.push([curr_idx + 1, curr_total, -1]);
        }
    }

    return cnt;
}

const numbers = [1, 1, 1, 1, 1];
const target = 3;
console.log(solution(numbers, target));