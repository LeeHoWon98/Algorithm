s = str(input())
n = int(input())
c = 0

result = []

for i in range(n):
    a = str(input())*2
    if s in a:
        c += 1

print(c)