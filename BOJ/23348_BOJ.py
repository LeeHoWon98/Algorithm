n1, n2, n3 = map(int, input().split())
count = int(input())
result = []

for i in range(count):
    value = 0
    for j in range(3):
        one, two, three = map(int, input().split())
        value += (one * n1) + (two * n2) + (three * n3)
    result.append(value)

print(max(result))