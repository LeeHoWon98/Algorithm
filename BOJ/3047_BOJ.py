nums = list(map(int, input().split()))
s = input()
nums.sort()

for i in s:
    if i == "A":
        print(nums[0], end = " ")
    elif i == "B":
        print(nums[1], end = " ")
    elif i == "C":
        print(nums[2], end = " ")