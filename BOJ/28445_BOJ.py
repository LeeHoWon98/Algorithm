import sys

s1 = set(sys.stdin.readline().split())
s2 = set(sys.stdin.readline().split())

s2.update(s1)
result = []

for i in s2:
    for j in s2:
        result.append([i, j])

result.sort(key=lambda x:(x[0], x[1]))

for k in result:
    print(*k)