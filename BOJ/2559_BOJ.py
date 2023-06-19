import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

result = sum(li[:m])
answer = result

for i in range(m, len(li)):
    result += li[i] - li[i - m]
    answer = max(answer, result)
    
print(answer)