s = input()
n = []

for i in range(len(s)):
    n.append(s[i:])

n.sort()

for j in n:
    print(j)