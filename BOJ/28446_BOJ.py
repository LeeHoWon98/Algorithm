import sys

n = int(sys.stdin.readline())
d = {}

for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 1:
        d[num[2]] = num[1]
    else:
        print(d[num[1]])