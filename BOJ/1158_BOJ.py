import sys
from collections import deque

n1, n2 = map(int,sys.stdin.readline().split())

q = deque(i for i in range(1, n1+1))
result = []

for j in range(n1):
    q.rotate(-(n2-1))
    result.append(q.popleft())
    
print('<' + ', '.join(map(str, result)) + '>')