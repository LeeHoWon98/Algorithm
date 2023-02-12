n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
result = 0

for i in range(len(nums2)):
    if nums2[i] == 0:
        result += nums1[i]

print(sum(nums1))
print(result)