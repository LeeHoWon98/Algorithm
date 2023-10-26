n1, n2 = map(int, input().split())
result = [input() for i in range(n1)]
col_s = ""
col = 0
row = 0

for i in result:
    if "X" not in i:
        row += 1

for j in range(n2):
    for k in range(n1):
        col_s += result[k][j]
    if "X" not in col_s:
        col += 1

print(min(col, row))