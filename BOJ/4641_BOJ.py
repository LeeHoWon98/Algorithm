while 1:
    c = 0
    n = list(map(int, input().split()))
    if len(n) == 1 and n[0] == -1:
        break
    else:
        n.sort()
        for i in range(1, len(n)):
            if n[i]*2 in n:
                c += 1
        print(c)