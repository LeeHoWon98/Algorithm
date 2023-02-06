n = int(input())
s = list(map(int, input().split()))
cnt = 1
sum = 0

for i in s:
    if i == 0:
        sum += 0
        cnt = 1
    else:
        sum = sum + i*cnt
        cnt += 1

print(sum)
