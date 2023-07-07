from itertools import permutations
import sys

n1 = int(sys.stdin.readline().rstrip())
n2 = int(sys.stdin.readline().rstrip())

nums = [sys.stdin.readline().rstrip() for i in range(n1)]
result = set()
    
for j in permutations(nums, n2):
    result.add(''.join(j))
    
print(len(result))