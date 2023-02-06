nums = []

for i in range(7):
    a = int(input())
    if a % 2 != 0:
        nums.append(a)

print(sum(nums))
print(min(nums))