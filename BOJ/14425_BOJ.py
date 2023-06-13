n1, n2 = map(int, input().split())
d = dict()

for i in range(n1):
   s1 = input()
   d[s1] = 0

for j in range(n2):
   s2 = input()
   if s2 in d:
      d[s2] += 1


print(sum(d.values()))