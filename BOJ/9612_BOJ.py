import sys

d = {}
n = int(sys.stdin.readline())

for i in range(n):
    word = sys.stdin.readline().rstrip()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

d = sorted(d.items(), key=lambda x:(x[1],x[0]))

print(*d[-1])