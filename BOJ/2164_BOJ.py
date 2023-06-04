from collections import deque

n1 = int(input())
q = deque([i for i in range(1, n1+1)])

for i in range(n1-1):
    q.popleft()
    n = q.popleft()
    q.append(n)
    
print(q[0])