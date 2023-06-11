import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(n):
    result = q.popleft()
    print(result[0], end=" ")
    if result[1] > 0:
        q.rotate(-(result[1]-1))
    elif result[1] < 0:
        q.rotate(-result[1])