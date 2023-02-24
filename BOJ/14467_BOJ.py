n = int(input())
result = {}
c = 0

for i in range(n):
    n1, n2 = map(int, input().split())
    if n1 not in result:
        result[n1] = n2
    else:
        if result[n1] != n2:
            c += 1
            result[n1] = n2
print(c)