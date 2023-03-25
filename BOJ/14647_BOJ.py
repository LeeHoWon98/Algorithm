n, m = map(int, input().split())
result = []
sum = 0
r, l = [], []

for i in range(n):
    c = 0
    num = input()
    sum += int(num.count("9"))
    c += int(num.count("9"))
    r.append(c)
    result.append(num.split())

for j in range(m):
    c2 = 0
    for k in range(n):
        c2 += result[k][j].count("9")
        l.append(c2)

print(sum - max(max(r), max(l)))