result = [j for j in range(1, 31)]
nums = []

for i in range(28):
    n = int(input())
    nums.append(n)

for k in result:
    if k not in nums:
        print(k)