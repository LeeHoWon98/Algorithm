n = int(input())
result = []

for i in range(n):
    n1, s1 = input().split()
    result.append([n1, s1])

result.sort(key=lambda x:(int(x[0])))

for j in result:
    print(*j)