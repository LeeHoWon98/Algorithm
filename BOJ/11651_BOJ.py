n = int(input())
result = []

for i in range(n):
    n1, n2 = map(int, input().split())
    result.append([n1, n2])

result.sort(key=lambda x:(x[1], x[0]))

for j in result:
    print(*j)