import sys

n = int(sys.stdin.readline())
result = 0
cost_li = []
c = 0

for i in range(n):
    name, cost = sys.stdin.readline().rstrip().split()
    if name == "jinju":
        result = int(cost)
    else:
        cost_li.append(int(cost))

for j in cost_li:
    if result < j:
        c += 1

print(result)
print(c)