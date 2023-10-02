n1, n2 = map(int, input().split())
result = []

for i in range(1, n2+1):
    for j in range(i):
        result.append(i)

print(sum(result[n1-1:n2]))