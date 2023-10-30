n = int(input())
nums = list(map(int, input().split()))
park = n//2

nums.sort()

print(sum(nums[:park]), sum(nums[park:]))