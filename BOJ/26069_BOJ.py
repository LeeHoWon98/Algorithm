n = int(input())
c = 0

d = {"ChongChong": 1}

for i in range(n):
    s1, s2 = input().split()
    
    if s1 in d or s2 in d:
        d[s1] = 1
        d[s2] = 1

for k, v in d.items():
    if v == 1:
        c += 1

print(c)