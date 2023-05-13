n, m = map(int, input().split())

nums = list(str(i) for i in range(1, n+1))

for j in range(m):
    s1, s2 = map(int, input().split())
    nums[s1-1], nums[s2-1] = nums[s2-1], nums[s1-1]
    
print(" ".join(nums))