n, m = map(int, input().split())

c = 0

for j in range(1, n+1):
    c += str(j).count(str(m))
        
print(c)