import sys

n1 = int(sys.stdin.readline())
d = {}
for i in range(n1):
    a, b = sys.stdin.readline().split()
    if b == 'enter':
        d[a] = i
    elif b == 'leave':
        d.pop(a)
        
result = sorted(d.keys(), reverse = True)

for j in result:
    print(j)