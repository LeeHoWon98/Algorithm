result = []

for i in range(5):
    result.append(input())

for j in range(15):
    for k in range(5):
        if j < len(result[k]):
            print(result[k][j], end = '')