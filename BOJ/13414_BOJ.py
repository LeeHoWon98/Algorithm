n1, n2 = map(int, input().split())
d = {}
c = 0

for i in range(n2):
    number = input()
    if number in d:
        del d[number]
        d[number] = 1
    else:
        d[number] = 1

for k, v in d.items():
    if c == n1:
        break
    else:
        print(k)
        c += 1