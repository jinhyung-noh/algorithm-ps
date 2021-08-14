import sys
from itertools import combinations


chars = {}
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    chars[alphabets[i]] = (1 << i) 

def word2bit(chars, word):
    bit = 0
    for char in word:
        bit = bit | chars[char]
    return bit

n = int(sys.stdin.readline())
words = [None] * n
for i in range(n):
    words[i] = word2bit(chars, sys.stdin.readline().strip())

cnt = 0
for i in range(1, n+1):
    for comb in combinations(range(n), i):
        test = 0
        for j in comb:
            test = test | words[j]
        if test == 67108863:
            cnt += 1

print(cnt)
    



