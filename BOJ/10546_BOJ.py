import sys
input= sys.stdin.readline

n = int(input())
d = dict()

for i in range(n):
    name = input().rstrip()
    if name in d:
        d[name] += 1
    else:
        d[name] = 1

for j in range(n-1):
    name = input().rstrip()
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
        
for k in d:
    if d[k] % 2 != 0:
        print(k)
        break