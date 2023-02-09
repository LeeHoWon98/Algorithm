n = int(input())

for i in range(n):
    num = int(input())
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))
    nums.clear()