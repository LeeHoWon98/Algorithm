def result(n1, n2):
    if n1 > n2:
        return
    print(n2)
    result(n1, n2-1)
n =int(input())
result(1,n)