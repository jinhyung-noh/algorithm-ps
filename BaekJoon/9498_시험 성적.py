import sys

score = int(sys.stdin.readline())

if score <= 100 and score >= 90:
    print("A")
elif score < 90 and score >= 80:
    print("B")
elif score < 80 and score >= 70:
    print("C")
elif score < 70 and score >= 60:
    print("D")
else:
    print("F")