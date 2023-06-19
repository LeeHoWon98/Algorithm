import sys
n1, n2 = map(int, sys.stdin.readline().split())
n_li = list(map(int, sys.stdin.readline().split()))

result = [0] * (len(n_li)+1)

for i in range(len(n_li)):
    result[i + 1] = result[i] + n_li[i]

for j in range(n2):
    left, right = map(int, sys.stdin.readline().split())
    print(result[right] - result[left - 1])