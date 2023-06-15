import sys
input = sys.stdin.readline

while 1:
    try:
        n, m = map(int, input().split())
    except:
        break
    c = 0
    for i in range(n, m+1):
        result1 = len(str(i))
        result2 = len(set(str(i)))
        if result1 != result2:
            continue
        else:
            c += 1    
    print(c)