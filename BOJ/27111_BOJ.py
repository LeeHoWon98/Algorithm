import sys

n = int(sys.stdin.readline())
d = {}
c = 0

for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n2 == 1:
        if n1 in d:
            c += 1
        else:
            d[n1] = n2
    else:
        if n1 in d:
            d.pop(n1)
        else:
            c += 1

print(c+len(d))