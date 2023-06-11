from collections import deque

n1 = int(input())

n_li = list(map(int, input().split()))
n_li.reverse()
q = deque()

for i in range(n1):
    if n_li[i] == 1:
        q.appendleft(i + 1)
    elif n_li[i] == 2:
        q.insert(1, i + 1)
    elif n_li[i] == 3:
        q.append(i + 1)
        
for j in q:
    print(j, end=" ")