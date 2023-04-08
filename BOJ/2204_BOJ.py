a = []
while True:
    n = int(input())
    if n != 0:
        for i in range(n):
            s = input()
            a.append(s)
            a.sort(key = lambda s: s.lower())
        print(a[0])
        a.clear()
    else:
        break