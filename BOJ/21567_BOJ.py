n1 = int(input())
n2 = int(input())
n3 = int(input())

s = str(n1 * n2 * n3)

for i in range(10):
    print(s.count(str(i)))