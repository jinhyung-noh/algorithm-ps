function solution(arr1, arr2) {
    const m = arr1.length;
    const n = arr1[0].length;

    // 빈 배열 만들기
    const arr = [];
    for (let i = 0; i < m; i++) {
        let row = []
        for (let j = 0; j < n; j++) {
            row.push(arr1[i][j] + arr2[i][j])
        }
        arr.push(row)
    }
    console.log(arr)
    return arr;
}

arr1 = [[1, 2], [2, 3]];
arr2 = [[3, 4], [5, 6]];
solution(arr1, arr2);