from collections import defaultdict

words = list(map(str, input().split()))

result = defaultdict(list)

for i in words:
    result["".join(sorted(i))].append(i)

print(list(result.values()))