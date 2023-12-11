n1, n2 = map(int, input().split())
li = list(map(int, input().split()))
c = 0

li.sort()

for i in li:
    if n1 < 200:
        n1 += i
        c += 1

print(c)