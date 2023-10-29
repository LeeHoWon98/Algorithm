import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    name, n1, n2, n3 = sys.stdin.readline().split()
    result.append([name, n1, n2, n3])

result.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in result:
    print(j[0])