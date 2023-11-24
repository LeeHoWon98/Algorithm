n = int(input())

for i in range(1, len(str(n))):
    n = int(round(n+0.00001, -i))

print(n)