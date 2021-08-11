import sys

# import mathematical way

a, b = [int(sys.stdin.readline()) for i in range(2)]

b_digits = []
_b = b

while _b > 0:
    b_digits.append(_b % 10)
    _b = _b // 10

print(a * b_digits[0])
print(a * b_digits[1])
print(a * b_digits[2])
print(a * b)


