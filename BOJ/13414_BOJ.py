import sys

n1, n2 = map(int, sys.stdin.readline().split())

d = {}

for i in range(n2):
    s = sys.stdin.readline().rstrip()
    d[s] = i

d = sorted(d.items(), key=lambda x:x[1])

if(n1 > len(d)):
    n1 = len(d)

for j in range(n1):
    print(d[j][0])