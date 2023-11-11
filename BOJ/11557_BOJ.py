n1 = int(input())

for i in range(n1):
    d = {}
    n2 = int(input())
    for j in range(n2):
        uni, num = input().split()
        d[uni] = num
        d = dict(sorted(d.items(), key=lambda x:-int(x[1])))
    print(list(d.keys())[0])