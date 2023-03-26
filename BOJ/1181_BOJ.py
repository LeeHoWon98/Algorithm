n = int(input())
s = []

for i in range(n):
    word = str(input())
    s.append(word)

s = list(set(s))
s.sort(key = lambda x:(len(x), x))

for j in s:
    print(j)