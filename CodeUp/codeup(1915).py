def result(n1):
    if n1 == 0:
        return 0
    elif n1 <= 2:
        return 1
    return result(n1-1) + result(n1-2)
num = int(input())
print(result(num))