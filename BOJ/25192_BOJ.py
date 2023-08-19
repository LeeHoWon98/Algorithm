n = int(input())
c = 0

d = {}

for i in range(n):
    s = input()
    if s == "ENTER":
        for k, v in d.items():
            if v == 1:
                c += 1
        d = {}
    else:
        if s not in d:
            d[s] = 1

for k, v in d.items():
    if v == 1:
        c += 1

print(c)