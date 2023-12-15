n = int(input())

result = []

for i in range(n):
    num, n1, n2, n3 = map(int, input().split())
    result.append([num, n1*n2*n3, n1+n2+n3])

result.sort(key=lambda x:(x[1], x[2], x[0]))

for i in range(3):
    print(result[i][0], end = " ")