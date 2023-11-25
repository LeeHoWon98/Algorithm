n = int(input())

for i in range(n):
    number = int(input())
    for j in range(len(str(number))):
        number = int(round(number+0.000001, -j))

    print(number)