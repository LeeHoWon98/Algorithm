n = int(input())
nums_sign = {"@" : 3, "%" : 5, "#" : 7}

for i in range(n):
    result = 0
    nums = list(input().split())
    for j in range(len(nums)):
        if j == 0:
            if nums[j].count(".") == 1:
                result += float(nums[j])
            else:
                result += int(nums[j])
        elif nums[j] == "@":
            result *= nums_sign[nums[j]]
        elif nums[j] == "%":
            result += nums_sign[nums[j]]
        elif nums[j] == "#":
            result -= nums_sign[nums[j]]
                
    print("{:.2f}".format(result))