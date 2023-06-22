import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

result = [0,li[0]]

for i in range(1, len(li)):
    result.append(result[i]+li[i])
    
for k in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(result[n2]-result[n1-1])