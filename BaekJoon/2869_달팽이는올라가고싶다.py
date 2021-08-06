import sys
import math

A, B, V = [int(i) for i in sys.stdin.readline().split()]

print(math.ceil((V-A) / (A-B)) + 1)