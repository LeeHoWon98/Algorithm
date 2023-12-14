import sys

n = int(sys.stdin.readline())
d = {}

for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
c = 0
for j in range(n):
    s = sys.stdin.readline().rstrip()
    if s in d:
        if d[s] != 0:
            c += 1
            d[s] -= 1

print(c)