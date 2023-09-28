while True:
    nd2 = []
    d = {}
    n1, n2 = map(int, input().split())
    if n1 == n2 == 0:
        break
    
    for i in range(n1):
        score = list(map(int, input().split()))
        for j in score:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    d = sorted(d.items(), key=lambda x:-x[1])
    d = dict(d)
    result = list(d.items())
    for k, v in d.items():
        if result[1][1] == v:
            nd2.append(k)
    nd2.sort()
    print(*nd2)