while 1:
    n = int(input())
    d = {}
    result = []
    if n == 0:
        break
    else:
        for i in range(n):
            name, cm = input().split()
            d[name] = float(cm)
        d = dict(sorted(d.items(), key=lambda x:-x[1]))
        for k, v in d.items():
            if max(d.values()) == v:
                result.append(k)
        print(*result)