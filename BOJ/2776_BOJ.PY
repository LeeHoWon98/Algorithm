t = int(input())
d = {}

for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    d = {}
    for j in li:
        d[j] = 1
    m = int(input())
    li2 = list(map(int, input().split()))
          
    for k in li2:
        if k in d:
            print(1)
        else:
            print(0)