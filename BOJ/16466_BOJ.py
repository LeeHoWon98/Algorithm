n = int(input())
nums = list(map(int, input().split()))

nums.sort()

for i in range(1, nums[-1]+1):
    if i != nums[i-1]:
        print(i)
        exit()
    
print(n+1)