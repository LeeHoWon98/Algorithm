a,b,c = map(int,input().split())
n1 = [0]*100
sum = 0

for i in range(3):
    s, e = map(int,input().split())
    for j in range(s, e):
        n1[j] += 1

for k in n1:
    if k != 0:
        if k == 1:
            sum += k*a
        elif k == 2:
            sum += k*b
        elif k == 3:
            sum += k*c

print(sum)