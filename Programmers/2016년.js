function solution(a, b) {
    // a가 몇월인지에 따라 더할 날짜수
    const monthes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 0];
    const totalDays = monthes.slice(0, a).reduce((acc, curr) => {
        return acc + curr;
    }, 0) + b;

    const days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    return days[totalDays % 7];
}

console.log(solution(5, 24));