import sys

n1, n2 = map(int, sys.stdin.readline().split())
d = dict()
result = []

for i in range(n1):
    name1 = sys.stdin.readline().rstrip()
    if name1 in d:
        d[name1] += 1
    else:
        d[name1] = 1
        
for j in range(n2):
    name2 = sys.stdin.readline().rstrip()
    if name2 in d:
        d[name2] += 1
    else:
        d[name2] = 1
        
for k in d:
    if d[k] == 2:
        result.append(k)

result.sort()

print(len(result))
print('\n'.join(result))