import sys

n = int(sys.stdin.readline())
result = []
answer = []

c = 0

for i in range(n):
    world, num, point = map(int, sys.stdin.readline().split())
    result.append([world, num, point])

result.sort(key=lambda x:-x[2])

print(result[0][0], result[0][1])
print(result[1][0], result[1][1])

if result[0][0] == result[1][0]:
    c = 1

for j in range(2, len(result)):
    if c == 0:
        print(result[j][0], result[j][1])
        break
    else:
        if result[1][0] != result[j][0]:
            print(result[j][0], result[j][1])
            break