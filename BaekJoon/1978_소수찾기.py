import sys

n = int(input())
nums = [int(i) for i in sys.stdin.readline().split()]

# get all primes under 1000
primes = [2]
for n in range(3,1001,2):
    is_prime = 1
    for prime in primes:
        if prime * prime > n:   # sqrt(n)까지만 조회
            break
        if n % prime == 0:  # n is not a prime
            is_prime = 0
            break
    if is_prime:
        primes.append(n)

cnt = 0
for num in nums:
    if num in primes:
        cnt += 1

print(cnt)


    
