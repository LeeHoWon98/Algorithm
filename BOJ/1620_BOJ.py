import sys

n1, n2 = map(int, sys.stdin.readline().split())
d1 = {}

for i in range(1, n1+1):
    name = sys.stdin.readline().rstrip()
    d1[i] = name
    d1[name] = i
    
for j in range(n2):
    result = sys.stdin.readline().rstrip()
    if result.isdigit():
        print(d1[int(result)])
    else:
        print(d1[result])