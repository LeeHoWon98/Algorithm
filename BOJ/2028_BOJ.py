n = int(input())

for i in range(n):
    num = input()
    result = int(num) ** 2
    if str(result)[-len(num):] == num:
        print("YES")
    else:
        print("NO")