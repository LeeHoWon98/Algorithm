n1 = int(input())
n2 = list(map(int, input().split()))

result = []
c = []

i = 0
while i < len(n2):
    result.append(n2[i])
    if i == len(n2) - 1 or n2[i] >= n2[i+1]:
        c.append(max(result) - min(result))
        result.clear()
    i += 1

print(max(c))