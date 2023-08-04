n = int(input())

result = []

for i in range(n):
    we, cm = map(int, input().split())
    result.append([we, cm])
    
for j in result:
    c = 1
    for k in result:
        if j[0] < k[0] and j[1] < k[1]:
            c += 1
    print(c, end = " ")