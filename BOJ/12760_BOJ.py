n1, n2 = map(int, input().split())
result = [0] * n1
answer = []

for i in range(n1):
    li = sorted(list(map(int, input().split())))
    answer.append(li)

for j in range(n2):
    max_value = []
    for k in range(n1):
        max_value.append(answer[k][j])
    mx = max(max_value)
    for l in range(n1):
        if mx == max_value[l]:
            result[l] += 1

mx_result = max(result)
last_value = []

for i in range(n1):
    if mx_result == result[i]:
        last_value.append(i+1)

print(*last_value)