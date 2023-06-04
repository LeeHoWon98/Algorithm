n1, n2 = map(int, input().split())
li = list(map(int, input().split()))
result = 0

for i in range(n1):
    for j in range(i+1, n1):
        for k in range(j+1, n1):
            if li[i] + li[j] + li[k] > n2:
                continue
            else:
                result = max(result, li[i] + li[j] + li[k])
                
print(result)