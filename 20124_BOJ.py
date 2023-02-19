num = int(input())
s = []

for i in range(num):
    name, point = input().split()
    point = int(point)
    s.append([name, point])

s.sort(key = lambda x:(-x[1], x[0]))

print(s[0][0])