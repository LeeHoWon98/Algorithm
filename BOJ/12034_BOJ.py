n = int(input())

for i in range(n):
    result = []
    num = int(input())
    price = list(map(int, input().split()))
    for j in range(1, num+1):
        anwser = price[-j]*0.75
        if anwser.is_integer():
            result.append(int(anwser))
            price.remove(int(anwser))
    result.sort()
    print("Case #"+str(i+1)+":", *result)