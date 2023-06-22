import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

result = [0] * (len(li)+1)

for i in range(len(li)):
    result[i + 1] = result[i] + li[i]
    
for k in range(m):
    n1, n2 = map(int, input().split())
    print(result[n2]-result[n1-1])