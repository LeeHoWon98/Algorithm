n = int(input())
names = []

for i in range(n):
    mto, mti = map(str, input().split())
    names.append([mto, mti])

names = sorted(names, key=lambda x:(x[0], x[1]), reverse=False)

for pair in names:
    print(pair[0], pair[1])