n1, n2 = map(int, input().split())
d = dict()
d2 = dict()

for i in range(1, n1+1):
    name = input()
    d[name] = i
    d2[i] = name
    
for j in range(n2):
    result = input()
    if result.isdigit():
        print(d2.get(int(result)))
    else:
        print(d.get(result))