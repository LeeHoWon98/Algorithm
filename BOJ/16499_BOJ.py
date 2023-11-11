import sys

while 1:
    n1, n2 = map(int,sys.stdin.readline().split())
    d = {}
    c = 0

    if n1 == 0 and n2 == 0:
        break
    
    for i in range(n1+n2):
        cd = int(sys.stdin.readline())
        if cd in d:
            d[cd] += 1
        else:
            d[cd] = 1
        
    for k,v in d.items():
        if v == 2:
            c += 1

    print(c)