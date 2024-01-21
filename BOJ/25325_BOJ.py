n = int(input())
name = list(input().split())
d = {}

for i in name:
    d[i] = 0

for i in range(n):
    new_name = list(input().split())
    for j in new_name:
        if j in d:
            d[j] += 1
            
d = sorted(d.items(), key=lambda x:(-x[1], x[0]))

for k, v in d:
    print(k, v)