N = int(input())
nums1 = list(map(int, input().split()))
d = dict()

for i in nums1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

M = int(input())
nums2 = list(map(int, input().split()))

for j in nums2:
    if j in d:
        print(d[j], end=" ")
    else:
        print(0, end=" ")