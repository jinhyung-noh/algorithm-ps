import sys
import bisect

# get all primes under 10000
primes = [2]
for n in range(3,10001,2):
    is_prime = 1
    for prime in primes:
        if prime * prime > n:   # sqrt(n)까지만 조회
            break
        if n % prime == 0:  # n is not a prime
            is_prime = 0
            break
    if is_prime:
        primes.append(n)


def goldbach_partition(target):
    closest_idx = bisect.bisect_right(primes, target // 2) - 1
    for idx in range(closest_idx, -1,-1):
        if primes[bisect.bisect_left(primes, target - primes[idx])] + primes[idx] == target:
            return (primes[idx], target-primes[idx])


answers = []
n = int(input())
for _ in range(n):
    target = int(sys.stdin.readline())
    answers.append(goldbach_partition(target))

for answer in answers:
    print(answer[0], answer[1])




