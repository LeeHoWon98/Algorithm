n = int(input())
d = dict()

for i in input().split():
    d[i] = 0

for j in range(n):
    for l in input().split():
        d[l] += 1

d = sorted(d.items(), key=lambda x:(-x[1], x[0]))

for kv in d:
    print(*kv)