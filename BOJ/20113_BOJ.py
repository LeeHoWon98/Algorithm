n = int(input())
numbers = list(map(int, input().split()))
d = {}
c = 0
s = ""

for i in numbers:
    if i in d:
        d[i] += 1
    elif i == 0:
        continue
    else:
        d[i] = 1

for k, v in d.items():
    if max(d.values()) == v:
        c += 1
        s += str(k)

if c == 1:
    print(s)
else:
    print("skipped")