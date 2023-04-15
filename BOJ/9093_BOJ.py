n1, n2 = map(int, input().split())

result = []

for i in range(1, n2):
    for k in range(i):
        if len(result) == n2:
            break
        else:
            result.append(i)

print(sum(result[n1-1:]))