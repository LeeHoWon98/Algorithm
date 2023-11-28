import sys

d = {}
n1, n2 = map(int, sys.stdin.readline().split())

for i in range(n2):
    name, won = sys.stdin.readline().split()
    if int(won) <= n1:
        if int(won) in d:
            d[int(won)] += [name]
        else:
            d[int(won)] = [name]

min_name = min([len(j) for j in d.values()])
min_won = min([j for j in d.keys() if len(d[j]) == min_name])

print(d[min_won][0], min_won)