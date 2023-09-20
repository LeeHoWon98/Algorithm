n1, n2, n3 = map(int, input().split())
d = {}

max_result = 0
min_result = 0

for i in range(n1):
    s, n = input().split()
    d[s] = int(n)

for j in range(n3):
    s1 = input()
    max_result += d[s1]
    min_result += d[s1]
    del d[s1]

d = sorted(d.items(), key=lambda x:-x[1])

for k in range(n2 - n3):
    max_result += d[k][1]
    min_result += d[-k-1][1]

print(min_result, max_result)