function solution(queue1, queue2) {
  const N = queue1.length + queue2.length;
  const sum1 = queue1.reduce((a, b) => a + b, 0);
  const sum2 = queue2.reduce((a, b) => a + b, 0);
  const totalSum = sum1 + sum2;

  if (totalSum % 2 === 1) {
    return -1;
  }
  let status1 = sum1 - totalSum / 2;
  let status2 = sum2 - totalSum / 2;
  let p1 = 0; // shift를 피하기 위한 포인터
  let p2 = 0;
  let count = 0;

  while (status1 !== status2 && count <= N + 3) {
    if (status1 > status2) {
      const pop = queue1[p1];
      queue2.push(pop);
      p1++;
      status1 -= pop;
      status2 += pop;
    } else {
      const pop = queue2[p2];
      queue1.push(pop);
      p2++;
      status1 += pop;
      status2 -= pop;
    }
    count++;
  }
  if (status1 === status2) {
    return count;
  }
  return -1;
}

const queue1 = [1, 2, 1, 2];
const queue2 = [1, 10, 1, 2];
const result = solution(queue1, queue2);
console.log(result);
