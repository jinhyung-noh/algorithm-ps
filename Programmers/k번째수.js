function solution(array, commands) {
    const results = [];

    for (let h = 0; h < commands.length; h++) {
        let [i, j, k] = commands[h];
        let sorted_arr = array.slice(i - 1, j);
        sorted_arr.sort();
        results.push(sorted_arr[k - 1]);
    }

    return results;
}

array = [1, 5, 2, 6, 3, 7, 4];
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];
console.log(solution(array, commands));