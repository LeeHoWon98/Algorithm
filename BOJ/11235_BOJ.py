n = int(input())
d = {}
result = []

for i in range(n):
    name = input()
    if name in d:
        d[name] += 1
    else:
        d[name] = 1

for k, v in d.items():
    if max(d.values()) == v:
        result.append(k)

result.sort()

for j in result:
    print(j)