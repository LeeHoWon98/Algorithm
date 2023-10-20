name = input()
nums = int(input())
name_li = [input() for i in range(nums)]
result = {}
result_li = []

for j in range(nums):
    L = name.count("L") + name_li[j].count("L")
    O = name.count("O") + name_li[j].count("O")
    V = name.count("V") + name_li[j].count("V")
    E = name.count("E") + name_li[j].count("E")

    result_c = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    result[name_li[j]] = result_c

max_r = max(result.values())

for k, v in result.items():
    if v == max_r:
        result_li.append(k)

if len(result_li) > 1:
    result_li.sort()
    print(result_li[0])
else:
    print(result_li[0])