while True:
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0:
        break

    d = {}
    c = 0

    for i in range(n1):
        n = int(input())
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    for i in range(n2):
        n = int(input())
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    for k, v in d.items():
        if v == 2:
            c += 1

    print(c)