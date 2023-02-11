nums = list(input().split())
num = input()
c = 0
for i in nums:
    if num in i[:len(num)] and num != i:
        c += 1

print(c)