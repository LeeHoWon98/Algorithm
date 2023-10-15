while 1:
    try:
        n = list(map(int, input().split(',')))
        print(sum(n))
    except:
        break