function solution(arr) {
    const stack = [];
    for (let i = 0; i < arr.length; i++) {
        console.log(stack[-1]);
        console.log(arr[i]);
        console.log("############");

        if (stack.length > 0 && arr[i] == stack[-1]) {
            console.log(i);
            continue;
        }
        stack.push(arr[i]);
    }
    return stack;
}

arr = [1, 1, 3, 3, 0, 1, 1];
console.log(solution(arr));