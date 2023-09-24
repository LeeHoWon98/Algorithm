a, b, c = map(int, input().split())
d = {}
sum = 0

for i in range(3):
    s, e = map(int, input().split())
    for j in range(s, e):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

for k, v in d.items():
    if v == 1:
        sum += v*a
    elif v == 2:
        sum += v*b
    elif v == 3:
        sum += v*c

print(sum)