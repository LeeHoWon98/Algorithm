n1, n2 = map(int, input().split())
c = 0

if n1 != 0:
    book = list(map(int, input().split()))
    total = book[0]

    for i in range(1, len(book)):
        total += book[i]
        if n2 < total:
            c += 1
            total = book[i]
            
    print(c+1)

else:
    print(c)