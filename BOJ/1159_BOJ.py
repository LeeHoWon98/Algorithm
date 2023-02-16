n = int(input())
s = []
result = []

for i in range(n):
    name = input()
    s.append(name[0])

for j in s:
    if s.count(j) >= 5:
        result.append(j)

if len(result) > 0:
    result1 = list(set(result))
    print("".join(sorted(result1)))

else:
    print("PREDAJA")