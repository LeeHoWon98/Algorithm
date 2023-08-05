n, d = map(int, input().split())
count = 0

result = [str(i) for i in range(1, n+1)]

for j in result:
    count += j.count(str(d))

print(count)