import sys

n = int(sys.stdin.readline())

result = []

for i in range(n):
    s1, s2, s3, s4 = sys.stdin.readline().split()
    result.append([s1, s2, s3, s4])

result.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in result:
    print(j[0])