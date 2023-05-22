def result(n1, n2):
    global sum
    if n1 > n2:
        return sum
    sum *= n1
    result(n1+1, n2)
num1 = int(input())
sum = 1
result(1, num1)
print(sum)