import sys
from collections import Counter
input = sys.stdin.readline

n1, n2, n3 = map(int, input().split())
result = []

for i in range(1, n1+1):
    for j in range(1, n2+1):
        for k in range(1, n3+1):
            sum = i + j + k
            result.append(sum)

c = Counter(result)

print(c.most_common(1)[0][0])