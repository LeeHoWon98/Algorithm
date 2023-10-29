import sys

n = int(sys.stdin.readline())
result = []
answer = []

for i in range(n):
    number, n1, n2, n3, n4 = map(int, sys.stdin.readline().split())
    result.append([number, n1, n2, n3, n4])

for j in range(1, 5):
    result.sort(key=lambda x:(-x[j], x[0]))
    answer.append(result[0][0])
    result.pop(0)

print(*answer)