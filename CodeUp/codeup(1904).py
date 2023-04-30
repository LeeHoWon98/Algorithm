def result(n1, n2):
    if n1 > n2:
        return
    else:
        if n1 % 2 != 0:
            print(n1, end=" ")
    result(n1+1, n2)
n1, n2 = map(int, input().split())
result(n1, n2)