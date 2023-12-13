c = 0
while 1:
    n = int(input())
    result = []
    
    if n == 0:
        break
    else:
        c += 1
        for i in range(n):
            result.append(input())
        
        result.sort()

        print(c)

        for j in result:
            print(j)