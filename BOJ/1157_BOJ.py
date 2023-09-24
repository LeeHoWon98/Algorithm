s = input()
s = s.lower()
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d = sorted(d.items(), key=lambda x:-x[1])

if len(d) >= 2 and d[0][1] == d[1][1]:
    print('?')
else:
    print(d[0][0].upper())