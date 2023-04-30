def result(n1, n2):
    if n1 > n2:
        return
    print(n1)
    result(n1+1, n)
n =int(input())
result(1,n)