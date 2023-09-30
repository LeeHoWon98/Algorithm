import sys

n1, n2 = map(int, sys.stdin.readline().split())
d = {}

for i in range(n1):
    s = sys.stdin.readline().rstrip()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

d = sorted(d.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
d = dict(d)

for k, v in d.items():
    if len(k) >= n2:
        print(k)