year_li = []
name_li = []

year_result = ""
name_result = ""

for i in range(3):
    po, year, name = input().split()
    year_li.append(int(year))
    name_li.append([int(po), name[0]])

year_li.sort()
name_li.sort(key=lambda x:-x[0])

for j in range(3):
    year_result += str(year_li[j]%100)
    name_result += name_li[j][1]

print(year_result)
print(name_result)