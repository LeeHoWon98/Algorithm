import sys

n1 = int(sys.stdin.readline())
s = []

for i in range(n1):
    s1 = int(sys.stdin.readline())
    if s1 == 0:
        s.pop()
    else:
        s.append(s1)

print(sum(s))