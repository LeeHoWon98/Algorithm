n1, n2 = map(int, input().split())

result1, result2 = "", ""

for i in range(n1):
    a = input()
    for j in a:
        result1 += j*2

for k in range(n1):
    b = input()
    result2 += b

if result1 == result2:
    print("Eyfa")

else:
    print("Not Eyfa")