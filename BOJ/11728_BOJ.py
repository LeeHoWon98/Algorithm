import sys

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a = a + b
a.sort()

print(' '.join(map(str, a)))