n = int(input())
result = []

for i in range(n):
    c, m, s = map(int, input().split())
    result.append([c, m, s])

result.sort()

for j in result:
    print(*j)