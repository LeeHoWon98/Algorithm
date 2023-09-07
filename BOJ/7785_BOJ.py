import sys

n = int(sys.stdin.readline())
d = {}

for i in range(n):
    n, s = sys.stdin.readline().split()
    d[n] = s

d = sorted(d.items(), key=lambda x:x[0], reverse=True)

for k, v in d:
    if v == "enter":
        print(k)