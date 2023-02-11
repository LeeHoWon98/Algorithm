n = int(input())
result = []

for i in range(n):
    s = input()
    c = s.count('for')+s.count('while')
    result.append(c)

print(max(result))