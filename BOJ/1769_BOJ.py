import sys

n = sys.stdin.readline().rstrip()
c = 0

while len(n) >= 2:
    result = 0
    for i in n:
        result += int(i)
    n = str(result)
    c += 1

print(c)

if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")