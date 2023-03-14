n = int(input())

for i in range(n):
    c = 0
    num = int(input())
    result1 = list(input().split())
    result2 = list(input().split())
    result1.sort()
    result2.sort()
    for j in range(len(result1)):
        if result1[j] != result2[j]:
            c += 1

    if c != 0:
        print('CHEATER')
    else:
        print('NOT CHEATER')