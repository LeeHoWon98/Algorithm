n = list(map(int, input()))
c = 0
result = 0

for i in range(0, len(n)-1):
    if n[i]+1 == n[i+1]:
        c += 1
    else:
        if c == 2:
            result += 1
            c = 0
        else:
            c = 0

if c == 2:
    result += 1
            
print(result)