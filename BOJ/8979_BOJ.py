n1, n2 = map(int, input().split())
result = []
c_result = []

for i in range(n1):
    n, g, s, d = map(int, input().split())
    result.append([n, g, s, d])

result.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(n1):
    c = 1
    for j in range(n1):
        if i == j:
            continue
        if result[i][1] < result[j][1] or (result[i][1] == result[j][1] and result[i][2] < result[j][2]) or (result[i][1] == result[j][1] and result[i][2] == result[j][2] and result[i][3] < result[j][3]):
            c += 1
    c_result.append([result[i][0], c])

for k, v in c_result:
    if k == n2:
        print(v)
        break