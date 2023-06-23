import sys

n1, n2 = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

window = sum(numbers[:n2])
result = [window]

for i in range(n2, len(numbers)):
    window += numbers[i] - numbers[i - n2]
    result.append(window)

if max(result) == 0:
    print('SAD')

else:
    print(max(result))
    print(result.count(max(result)))