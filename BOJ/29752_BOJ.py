n = int(input())
nums = list(map(int, input().split()))
c = 0
result = []

for i in nums:
    if i == 0:
        c = 0
    else:
        c += 1
    result.append(c)

print(max(result))