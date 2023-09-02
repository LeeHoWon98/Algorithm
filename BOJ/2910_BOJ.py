import sys

n1, n2 = map(int, sys.stdin.readline().split())

d = {}

s = list(sys.stdin.readline().rstrip().split())
idx = 1

for i in s:
    if i in d:
        d[i][0] += 1
    else:
        d[i] = [1, idx]
        idx += 1

d = sorted(d.items(), key=lambda x:(-x[1][0], x[1][1]))

result = []

for v, c in d:
    result.append((v+" ")*c[0])
    
print("".join(result))