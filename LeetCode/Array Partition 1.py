n = int(input())
nums = list(map(int, input().split()))
result = []

for i in range(1, len(nums)-1):
    if nums[i+1] - nums[i] != 1:
        result.append(nums[i+1])

print(sum(result)+nums[0])