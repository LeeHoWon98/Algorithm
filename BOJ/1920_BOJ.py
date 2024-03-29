def binary_search(s, e, num1, j):
    while s <= e:
        mid = (s+e) // 2

        if num1[mid] == j:
            return 1
        elif num1[mid] < j:
            s = mid+1
        else:
            e = mid-1
    return 0

n1 = int(input())
num1 = list(map(int, input().split()))
n2 = int(input())
num2 = list(map(int, input().split()))

num1.sort()

for j in num2:
    print(binary_search(0, n1-1, num1, j))