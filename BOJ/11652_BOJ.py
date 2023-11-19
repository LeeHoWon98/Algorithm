import sys

n = int(sys.stdin.readline())
d = {}

for i in range(n):
    number = int(sys.stdin.readline())
    if number in d:
        d[number] += 1
    else:
        d[number] = 1

result = sorted(d.items(), key=lambda x:(-x[1], x[0]))

print(result[0][0])