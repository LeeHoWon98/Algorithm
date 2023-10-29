import sys

n = int(sys.stdin.readline())
s = set(map(int, input().split()))

result = list(s)
result.sort()

print(*result)