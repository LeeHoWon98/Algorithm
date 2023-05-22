def result(n1):
    if n1 == 1:
        print(int(n1))
        return
    else:
        print(int(n1))
        if n1 % 2 == 1:
            result(3*n1+1)
        else:
            result(n1//2)
 
num = int(input())
result(num)